def approximate_pi(n_terms):
    if n_terms <= 0:
        return 0.0
    leibniz_series = [((-1) ** n) / (2 * n + 1) for n in range(n_terms)]
    return 4 * sum(leibniz_series)

