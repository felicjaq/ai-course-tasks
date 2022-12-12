import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

apple = [131.96, 121.26, 122.15, 131.46, 124.61, 136.96,
         145.86, 151.83, 141.50, 149.80, 165.30, 177.57]

google = [91.79, 101.84, 103.43, 120.51, 120.58, 125.32,
          135.22, 145.46, 133.27, 148.27, 142.45, 144.68]

microsoft = [231.96, 232.38, 235.77, 252.18, 249.68, 270.90,
             284.91, 301.88, 281.92, 331.62, 330.59, 336.32]

months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл',
          'Авг', 'Сен', 'Окт', 'Нояб', 'Дек']

plt.plot(months, apple)
plt.plot(months, microsoft)
plt.plot(months, google)
plt.title('Стоимость 1 акции корпораций Apple, Google и ' '\n'
          'Microsoft за каждый месяц 2021 года:')
plt.grid()

fig, ax = plt.subplots()

ax.plot(months, microsoft, label='Microsoft')
ax.plot(months, apple, label='Apple')
ax.plot(months, google, label='Google')

ax.legend()

ax.yaxis.set_major_locator(ticker.MultipleLocator(25))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.grid(which='major', color='k')

ax.minorticks_on()

ax.grid(which='minor', color='gray', linestyle=':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.title('Стоимость 1 акции корпорации' '\n'
          'за каждый месяц 2021 года: ($)')
plt.show()
