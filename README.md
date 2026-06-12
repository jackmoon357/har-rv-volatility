# HAR-RV + ML overlay for USDZAR realised volatility

Forecasting daily realised volatility of the USD/ZAR exchange rate using the HAR-RV model (Corsi, 2009) as a baseline, extended with an XGBoost overlay on engineered features. Out-of-sample evaluation uses RMSE, MAE, and QLIKE, with Diebold-Mariano tests for significance.

**Status:** work in progress. Currently at Phase 0 (scaffolding) of 9.

## Motivation

USDZAR is one of the most-traded emerging-market currencies and a textbook risk-on/risk-off barometer. Accurate short-horizon volatility forecasts feed into VaR, option pricing, and carry-trade risk management. The HAR-RV model captures long-memory behaviour in realised volatility parsimoniously; the question this project asks is whether a tree-based ML overlay on richer features (semivariance, bipower variation, leverage proxies, overnight returns) can improve on HAR out-of-sample by a margin that is both economically and statistically significant.

## Method (planned)

- **Data:** USDZAR intraday quotes, 2010-01 to 2024-12, sampled at 5 minutes for RV construction (microstructure-noise sweet spot).
- **Baseline:** HAR-RV regression on log-RV with daily, weekly (5-day), and monthly (22-day) components, HAC standard errors.
- **Overlay:** XGBoost predicting either log-RV directly or the HAR residual, tuned on a contiguous validation set.
- **Split:** chronological. Train 2010–2020, validate 2021–2022, test 2023–2024. No shuffling. Test set touched once.
- **Evaluation:** RMSE, MAE, QLIKE (Patton, 2011), Diebold-Mariano test.

## Repository structure

```
.
├── data/              # gitignored; see data/raw/README.md for source instructions
├── notebooks/         # exploration, audits, figures
├── src/har_rv/        # reproducible pipeline modules
├── tests/             # unit tests for RV estimator and HAR fit
├── paper/             # LaTeX source for the research note
├── pyproject.toml     # dependencies
└── uv.lock            # pinned environment
```

## Reproduction

```bash
git clone https://github.com/jackmoon357/har-rv-volatility
cd har-rv-volatility
uv sync
```

Data acquisition instructions live in `data/raw/README.md`. End-to-end pipeline command will be added in Phase 9.

## References

- Corsi, F. (2009). A Simple Approximate Long-Memory Model of Realized Volatility. *Journal of Financial Econometrics*, 7(2), 174–196.
- Andersen, T.G., Bollerslev, T., Diebold, F.X., Labys, P. (2003). Modeling and Forecasting Realized Volatility. *Econometrica*, 71(2), 579–625.
- Patton, A.J. (2011). Volatility Forecast Comparison Using Imperfect Volatility Proxies. *Journal of Econometrics*, 160(1), 246–256.

## Author

Jack Moon, Stellenbosch University.

## License

MIT (see `LICENSE`).