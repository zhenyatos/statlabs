from scipy import stats
import math


def interval_mle(samples, alpha):
    m, s = stats.norm.fit(samples)
    n = len(samples)

    t = stats.t(n-1)
    chi2 = stats.chi2(n-1)

    m_delta = s * t.ppf(1 - alpha / 2) / math.sqrt(n-1)
    m_l = m - m_delta
    m_r = m + m_delta
    s_l = s * math.sqrt(n / chi2.ppf(1 - alpha / 2))
    s_r = s * math.sqrt(n / chi2.ppf(alpha / 2))

    return [m_l, m_r], [s_l, s_r]


def interval_asympt(samples, alpha):
    m, s = stats.norm.fit(samples)
    n = len(samples)
    e = stats.kurtosis(samples)

    u = stats.norm(0, 1)

    m_delta = s * u.ppf(1 - alpha / 2) / math.sqrt(n)
    m_l = m - m_delta
    m_r = m + m_delta
    U = u.ppf(1 - alpha / 2) * math.sqrt((e + 2) / n)
    s_l = s * math.pow(1 + U, -1/2)
    s_r = s * math.pow(1 - U, -1/2)

    return [m_l, m_r], [s_l, s_r]

