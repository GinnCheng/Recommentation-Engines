import numpy as np
from scipy import stats
def experiment_size(p_null, p_alt, alpha = .05, beta = .20):
        """
        Compute the minimum number of samples needed to achieve a desired power
        level for a given effect size.
        Input parameters:
            p_null: base success rate under null hypothesis
            p_alt : desired success rate to be detected
            alpha : Type-I error rate
            beta  : Type-II error rate
        Output value:
            n : Number of samples required for each group to obtain desired power
        """
        # Get necessary z-scores and standard deviations (@ 1 obs per group)
        z_null = stats.norm.ppf(1 - alpha)
        z_alt  = stats.norm.ppf(beta)
        sd_null = np.sqrt(p_null * (1-p_null) + p_null * (1-p_null))
        sd_alt  = np.sqrt(p_null * (1-p_null) + p_alt * (1-p_alt))
        # Compute and return minimum sample size
        p_diff = p_alt - p_null
        n = ((z_null*sd_null - z_alt*sd_alt) / p_diff) ** 2
        return np.ceil(n)

N = experiment_size(0.02, 0.023, alpha = .05/2, beta = .20)
print(N)

# power.prop.test(p1 = 0.16, p2 = 0.175, sig.level = 0.05, power = 0.8, alternative = "greater")


# from scipy.stats import norm, zscore
#
# def sample_power_probtest(p1, p2, power=0.8, sig=0.05):
#     z = norm.isf([sig/2]) #two-sided t test
#     zp = -1 * norm.isf([power])
#     d = (p1-p2)
#     s =2*((p1+p2) /2)*(1-((p1+p2) /2))
#     n = s * ((zp + z)**2) / (d**2)
#     return int(round(n[0]))
#
# def sample_power_difftest(d, s, power=0.8, sig=0.05):
#     z = norm.isf([sig/2])
#     zp = -1 * norm.isf([power])
#     n = s * ((zp + z)**2) / (d**2)
#     return int(round(n[0]))
#
# if __name__ == '__main__':
#
#     n = sample_power_probtest(0.16, 0.175, power=0.8, sig=0.025)
#     print(n)  #14752
#
#     n = sample_power_difftest(0.16, 0.175, power=0.8, sig=0.025)
#     print(n)  #392