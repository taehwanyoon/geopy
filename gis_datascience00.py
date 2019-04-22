import geopandas as gpd
import matplotlib
matplotlib.use('Tkagg')
import matplotlib.pyplot as plt
gpd.__version__

countries = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

countries.tail(3)
cities.tail(3)

ax = countries.plot(column="continent", legend=True, categorical=True)
ax.set_title("세계 지도")
ax.set_axis_off()
plt.show()

# 만약, 표현하고 싶은 컬럼이 실수 변수라면, 색을 변화시키는 기준 즉 데이터를 구분하는 방법과 갯수를 정의할 수 있다. 먼저 구분하는 방법은 plot()명령의
# scheme 인자로 설정하는데, 지원하는 것으로는 "Equal_interval"(동일한 간격으로 구분), "Quantiles"(4분위수를 구하여 구분), "Fisher_Jenks"
# (클래스 내 분산을 줄이고, 클래스 끼리의 분산을 최대화하는 방식으로 구분)가 있다. 구분하는 갯수는 k 인자에 원하는 숫자를 입력하면된다. 디폴트는 5이다.
#
# 다음 코드는 국가별 GDP 추정치를 해당 국가의 추정인구로 나누어, 추정 1인당 GDP를 만들고, 이를 지도에서 색으로 표현한 예이다.
#
# 추가적으로, 정보를 색으로 나타낼 때는 표현하려는 정보에 따라, 컬러맵을 설정하는 것이 좋다. 이 예와 같이 수치적인 정보를 시각화 할 때는, 수치만큼 색이
# 밝고 어두워지는 것으로 표현하는 것이 더 적절하기 때문에 Sequence 계열의 컬러맵을 설정하는 것이 좋다. 컬러맵에 대해서는 이 곳을 참고하길 바란다.
# (https://matplotlib.org/users/colormaps.html)

countries['gdp_per_cap'] = countries['gdp_md_est'] / countries['pop_est'] * 100

ax = countries.plot(column='gdp_per_cap', legend=True, scheme='quantiles', cmap='Blues', k=5)
ax.set_title('gdp per capita')
ax.set_axis_off()
plt.show()

countries.geom_type[:3]
print(countries.geometry[113])
countries.geometry[113]

cities.geom_type[:3]

base = countries.plot(color='white', edgecolor="k")
ax = cities.plot(ax=base, marker='o', color='red', markersize=5)
ax.set_axis_off()
ax.set_title("세계 도시 분포")
plt.show()

korea_border = countries[countries.name == 'Korea'].geometry
korea_border.boundary.squeeze()