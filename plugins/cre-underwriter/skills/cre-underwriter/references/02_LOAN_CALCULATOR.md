# EBSC LOAN CALCULATOR
## Authoritative Calculator Specification and Implementation

---

# 1. PURPOSE

This file is the sole authority for EBSC calculator-generated outputs.

The Master Operating System may call and consume these outputs, but it must not recreate, approximate, or duplicate the calculator formulas contained here.

The Client Email Draft uses the borrower's Requested Loan Amount as the calculator Loan Amount input.

The calculator controls:

- Loan Amount validation.
- Loan Term validation.
- Static Interest Rate validation.
- Origination Fee ($).
- Origination Points (%).
- Interest-only monthly payment.
- Total Interest (Term).
- Final Payment (Principal + Interest).
- Total Payment (Principal + Interest).

---

# 2. CONTROLLING INPUTS

## Requested Loan Amount

Minimum:

**$5,000,000**

Maximum:

**$250,000,000**

Step:

**1 whole dollar**

The calculator must use the borrower's Requested Loan Amount.

Do not substitute:

- LTV sizing.
- LTC sizing.
- DSCR sizing.
- Underwriter sizing.
- Recommended sizing.
- Any alternate amount.

## Loan Term

Minimum:

**1 month**

Maximum:

**120 months**

The term is entered and evaluated in months only.

Do not clamp, shorten, convert, or replace the submitted term.

## Interest Rate

**9.76%**

The Interest Rate is static and read-only.

## Payment Structure

**Interest Only**

---

# 3. VALIDATION MESSAGES

Use these validation messages exactly:

**Loan amount is required.**

**Loan amount must be between $5,000,000 and $250,000,000.**

**Enter a valid interest rate.**

**Loan term is required.**

**Loan term must be between 1 and 120 months.**

A missing Loan Term does not prevent valid Origination Fee and Origination Points output after a valid Loan Amount is entered.

Payment calculations require a valid Loan Amount and valid Loan Term.

---

# 4. ORIGINATION FEE AUTHORITY

The calculator contains one authoritative origination-fee function.

Controlling parameters:

```javascript
const minLoan = 5_000_000;
const maxLoan = 250_000_000;
const minFee  = 275_000;
const maxFee  = 2_750_000;
```

Origination Fee is calculated by linear interpolation between the minimum and maximum loan/fee endpoints.

The controlling value is the Origination Fee ($).

Origination Points (%) are derived from the calculated fee and Requested Loan Amount.

---

# 5. AUTHORITATIVE ORIGINATION FEE FUNCTION

```javascript
function calcOriginationFee(loanAmount) {
  const minLoan = 5_000_000;
  const maxLoan = 250_000_000;
  const minFee  = 275_000;
  const maxFee  = 2_750_000;

  if (!Number.isFinite(loanAmount)) return null;
  if (loanAmount < minLoan || loanAmount > maxLoan) return null;

  const position = (loanAmount - minLoan) / (maxLoan - minLoan);
  return minFee + position * (maxFee - minFee);
}
```

Do not create a second fee function.

Do not create:

- A fee table.
- A second pricing curve.
- Alternate fee anchors.
- A fallback pricing formula.
- A manual substitute fee.

---

# 6. ORIGINATION POINTS

Origination Points are implied from the controlling Origination Fee.

```javascript
function calcOriginationPoints(loanAmount, originationFee) {
  if (!Number.isFinite(loanAmount) || loanAmount <= 0) return null;
  if (!Number.isFinite(originationFee)) return null;

  return (originationFee / loanAmount) * 100;
}
```

Display Origination Points to two decimal places.

The underlying Origination Fee remains the controlling value.

Origination Points and Origination Fee must display as soon as a valid Loan Amount is available, even when the Loan Term is still missing.

---

# 7. INTEREST-ONLY PAYMENT CALCULATIONS

Use the static annual Interest Rate of 9.76%.

```javascript
const ANNUAL_RATE = 0.0976;
```

## Monthly Interest-Only Payment

```javascript
function calcMonthlyInterestOnlyPayment(loanAmount) {
  return loanAmount * ANNUAL_RATE / 12;
}
```

## Total Interest for the Term

```javascript
function calcTotalInterest(loanAmount, termMonths) {
  const monthlyPayment = calcMonthlyInterestOnlyPayment(loanAmount);
  return monthlyPayment * termMonths;
}
```

## Final Payment (Principal + Interest)

The final payment consists of the full principal balance plus the final month's interest payment.

```javascript
function calcFinalPayment(loanAmount) {
  const monthlyPayment = calcMonthlyInterestOnlyPayment(loanAmount);
  return loanAmount + monthlyPayment;
}
```

## Total Payment (Principal + Interest)

```javascript
function calcTotalPayment(loanAmount, termMonths) {
  const totalInterest = calcTotalInterest(loanAmount, termMonths);
  return loanAmount + totalInterest;
}
```

---

# 8. DISPLAY LABELS

Use these labels:

**Requested Loan Amount**

**Origination Points (%)**

**Origination Fee ($)**

**Total Interest (Term)**

**Final Payment (Principal + Interest)**

**Total Payment (Principal + Interest)**

Payment Structure is:

**Interest Only**

---

# 9. DISPLAY ORDER AND CALCULATION TIMING

When the user enters a valid Requested Loan Amount:

1. Validate Loan Amount.
2. Calculate Origination Fee.
3. Calculate Origination Points.
4. Display Origination Fee and Origination Points immediately.

Do not wait for Loan Term before showing Origination Fee or Origination Points.

When a valid Loan Term is also available:

1. Validate Loan Term.
2. Calculate Monthly Interest-Only Payment.
3. Calculate Total Interest (Term).
4. Calculate Final Payment (Principal + Interest).
5. Calculate Total Payment (Principal + Interest).

If the Loan Term is missing:

- Keep valid Origination Fee displayed.
- Keep valid Origination Points displayed.
- Do not invent a term.
- Payment outputs that require the term remain unavailable.
- Return the validation message **Loan term is required.**

---

# 10. COMPLETE REFERENCE CALCULATION FUNCTION

```javascript
function calculateEBSC(loanAmount, termMonths) {
  const minLoan = 5_000_000;
  const maxLoan = 250_000_000;
  const minTerm = 1;
  const maxTerm = 120;
  const annualRate = 0.0976;

  const errors = [];

  if (loanAmount === null || loanAmount === undefined || loanAmount === "") {
    errors.push("Loan amount is required.");
  } else if (!Number.isFinite(Number(loanAmount)) || Number(loanAmount) < minLoan || Number(loanAmount) > maxLoan) {
    errors.push("Loan amount must be between $5,000,000 and $250,000,000.");
  }

  if (!Number.isFinite(annualRate) || annualRate <= 0) {
    errors.push("Enter a valid interest rate.");
  }

  const amount = Number(loanAmount);
  const amountValid = Number.isFinite(amount) && amount >= minLoan && amount <= maxLoan;

  let originationFee = null;
  let originationPoints = null;

  if (amountValid) {
    originationFee = calcOriginationFee(amount);
    originationPoints = calcOriginationPoints(amount, originationFee);
  }

  if (termMonths === null || termMonths === undefined || termMonths === "") {
    errors.push("Loan term is required.");

    return {
      requestedLoanAmount: amountValid ? amount : null,
      annualInterestRate: 0.0976,
      interestRateDisplay: "9.76%",
      rateType: "Fixed",
      paymentStructure: "Interest Only",
      termMonths: null,
      loanTermDisplay: "To Be Confirmed",
      originationFee,
      originationPoints,
      monthlyPayment: null,
      totalInterest: null,
      finalPayment: null,
      totalPayment: null,
      errors
    };
  }

  const term = Number(termMonths);
  const termValid = Number.isInteger(term) && term >= minTerm && term <= maxTerm;

  if (!termValid) {
    errors.push("Loan term must be between 1 and 120 months.");
  }

  if (!amountValid || !termValid) {
    return {
      requestedLoanAmount: amountValid ? amount : null,
      annualInterestRate: 0.0976,
      interestRateDisplay: "9.76%",
      rateType: "Fixed",
      paymentStructure: "Interest Only",
      termMonths: termValid ? term : null,
      loanTermDisplay: termValid ? `${term} months` : null,
      originationFee,
      originationPoints,
      monthlyPayment: null,
      totalInterest: null,
      finalPayment: null,
      totalPayment: null,
      errors
    };
  }

  const monthlyPayment = amount * annualRate / 12;
  const totalInterest = monthlyPayment * term;
  const finalPayment = amount + monthlyPayment;
  const totalPayment = amount + totalInterest;

  return {
    requestedLoanAmount: amount,
    annualInterestRate: annualRate,
    interestRateDisplay: "9.76%",
    rateType: "Fixed",
    paymentStructure: "Interest Only",
    termMonths: term,
    loanTermDisplay: `${term} months`,
    originationFee,
    originationPoints,
    monthlyPayment,
    totalInterest,
    finalPayment,
    totalPayment,
    errors
  };
}
```

---

# 11. FORMATTING

Currency outputs should be formatted as United States dollars with appropriate separators and cents where applicable.

Example:

**$349,553.06**

Percentage outputs should display two decimal places where applicable.

Example:

**2.82%**

Do not alter the underlying unrounded controlling value merely for display purposes.

---

# 12. PRELIMINARY SOFT QUOTE INTEGRATION

The Preliminary Soft Quote receives these calculator-controlled values:

- Origination Points (%).
- Origination Fee ($).

The calculator input for these values is the Requested Loan Amount.

The Preliminary Soft Quote does not independently calculate pricing.

A missing Loan Term does not prevent these two pricing outputs from being supplied when the Requested Loan Amount is valid.

---

# 13. CALCULATOR OUTPUT OBJECT

The calculator should make the following values available to the Master Operating System when valid:

```javascript
{
  requestedLoanAmount,
  annualInterestRate,
  interestRateDisplay,
  rateType,
  paymentStructure,
  termMonths,
  loanTermDisplay,
  originationFee,
  originationPoints,
  monthlyPayment,
  totalInterest,
  finalPayment,
  totalPayment,
  errors
}
```

The Master Operating System consumes these values.

It does not recreate them.

---

# 14. CALCULATOR FAILURE BEHAVIOR

If Loan Amount is invalid:

- Do not calculate Origination Fee.
- Do not calculate Origination Points.
- Do not calculate payment outputs.
- Return the applicable validation message.

If Loan Amount is valid but Loan Term is missing:

- Calculate Origination Fee.
- Calculate Origination Points.
- Display **To Be Confirmed** for Loan Term / Maturity in the Preliminary Soft Quote.
- Return **Loan term is required.**
- Do not calculate term-dependent payment outputs.

If Loan Amount is valid but Loan Term is outside 1 to 120 months:

- Preserve valid Origination Fee and Origination Points.
- Return **Loan term must be between 1 and 120 months.**
- Do not clamp or convert the term.
- Do not calculate term-dependent payment outputs.

---

# 15. OUTPUT AND FEATURE BOUNDARY

The calculator does not generate a PDF.

Calculator output is consumed by the Master Operating System and Client Email Draft process.

The calculator must not:

- Rewrite the Client Email Draft.
- Determine underwriting findings.
- Determine eligibility.
- Determine final credit approval.
- Change the Requested Loan Amount.
- Change the Preliminary Soft Quote structure.
- Alter the Word Client Email Draft template.

---

# 16. REGRESSION TESTS

The following conditions must pass before this calculator is treated as production-valid.

## Loan Amount

- $4,999,999 → invalid.
- $5,000,000 → valid.
- $250,000,000 → valid.
- $250,000,001 → invalid.

## Origination Fee Endpoints

- $5,000,000 → $275,000.00.
- $250,000,000 → $2,750,000.00.

## Known Interior Test

- $12,380,000 → Origination Fee approximately $349,553.06.
- $12,380,000 → Origination Points approximately 2.82%.

## Loan Term

- Missing → `Loan term is required.` and Loan Term / Maturity = `To Be Confirmed`.
- 0 months → invalid.
- 1 month → valid.
- 120 months → valid.
- 121 months → invalid.

## Interest Rate

- Static display = 9.76%.
- Read-only behavior preserved.

## Payment Structure

- Interest Only.

## Pricing Timing

- Valid Loan Amount alone displays Origination Fee and Origination Points.
- Loan Term is not required for pricing output.
- Loan Term is required for term-dependent payment outputs.

## Labels

- Requested Loan Amount.
- Total Interest (Term).
- Final Payment (Principal + Interest).
- Total Payment (Principal + Interest).

---

# 17. GOVERNING PRINCIPLE

The approved EBSC Loan Calculator is the single source of truth for calculator-generated values.

The Requested Loan Amount drives pricing.

Origination Fee is the controlling pricing output.

Origination Points are implied from the Origination Fee.

The rate remains fixed at 9.76%.

The payment structure remains Interest Only.

The term range remains 1 to 120 months.

The loan range remains $5,000,000 to $250,000,000.

The Master Operating System uses these outputs without creating a second calculator implementation.