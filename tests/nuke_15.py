import numpy as np


if __name__ == "__main__":
    e1 = (250 * 112) / (77 + 112)
    e2 = (250 * 77) / (77 + 112)
    i_random = 13212 + 10358
    s_i_random = np.sqrt(69 * 69 + 64 * 64)
    s_i_alpha = 455
    i_alpha = 1230235
    s_p = np.sqrt(
        (2 * i_alpha * s_i_random / (i_random + 2 * i_alpha) ** 2) ** 2
        + (2 * s_i_alpha * i_random / (i_random + 2 * i_alpha) ** 2)
    )
    p_alpha = 2 * i_alpha / (i_random + 2 * i_alpha)
    p_random = i_random / (2 * i_alpha + i_random)
    s_k = np.sqrt(
        (s_i_random / (2 * i_alpha)) ** 2
        + (s_i_alpha * i_random / (2 * i_alpha**2)) ** 2
    )
    t_half_div_years = 2.65
    t_half_div_alpha = t_half_div_years / p_alpha
    s_t_half_div = t_half_div_years * s_p / p_alpha**2
    t_half_div_random = t_half_div_years / p_random

    print(s_k)
