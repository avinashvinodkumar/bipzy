playwright-saucedemo/
│
├── tests/
│   ├── sort.spec.ts            # Sorting tests (Z-A, High-Low)
│   ├── cart-checkout.spec.ts   # Cart & Checkout journey
│   ├── visual.spec.ts          # Visual regression (bonus)
│   ├── accessibility.spec.ts   # Accessibility tests (bonus)
│
├── pages/                      # Page Object Models
│   ├── login.page.ts
│   ├── inventory.page.ts
│   ├── cart.page.ts
│   ├── checkout.page.ts
│
├── utils/
│   ├── helpers.ts              # Utility functions (e.g., login helper)
│   └── visualHelper.ts         # Visual regression config (if using Percy or similar)
│
├── tests-execution/
│   ├── reports/
│   └── logs/
│
├── .github/
│   └── workflows/ci.yml        # Optional: GitHub Actions for CI/CD (extra credit)
│
├── playwright.config.ts
├── package.json
└── README.md
