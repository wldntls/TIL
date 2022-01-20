# Folium 라이브러리-지도 활용

## 1.  설치

- Mac
  - 터미널 실행 
  - `conda install -c conda-forge folium` 입력 (아나콘다 설치되어 있다는 가정하에)
  - 설치 완료!



## 2. 지도 만들기

- ````python
  import folium # folium 라이브러리 불러오기
  
  seoul_map= folium.Map(location=[37.55,126.98],zoom_start=12) 
  # seoul_map에 위도37.55, 경도 126.98, 확대 12(기본값 10) 의 지도 만들어 할당하기
  
  seoul_map # 출력
  seoul_map.save('./seoul.html') # 현재 디렉토리에 html 파일로 생성
  ````



## 3. 지도 스타일 적용하기

- ````python
  import folium
  
  seoul_map2 = folium.Map(location=[37.55,126.98],tiles='Stamen Terrain',zoom_start=12) 
  # Stamen Terrain 스타일로 지도 생성
  seoul_map3 = folium.Map(location=[37.55,126.98],tiles='Stamen Toner',zoom_start=15)
  # Stamen Toner 스타일로 지도 생성
  
  seoul_map2.save('./seoul2.html') # 현재 디렉토리에 html 파일로 생성
  seoul_map3.save('./seoul3.html') # 현재 디렉토리에 html 파일로 생성
  ````



## 4. 지도에 마커 표시하기

- 지도에 마커 표시하기 

  - ````python
    import pandas as pd
    import folium
    
    df = pd.read_excel('./서울지역 대학교 위치.xlsx') # 같은 폴더에 있는 엑셀 데이터 불러오기
    
    seoul_map = folium.Map(location=[37.55,126.98],tiles='Stamen Terrain', zoom_start = 12)
    # seoul_map에 위도37.55, 경도 126.98, 확대 12(기본값 10) 의 지도 만들어 할당하기
    
    for name, lat, lng in zip(df.index, df.위도, df.경도): 
      # index(학교로 바꾸면 학교 이름이 나옴), 위도, 경도를 각 변수에 할당하면서 for문 돌리기
        folium.Marker([lat,lng],popup=name).add_to(seoul_map) 
        # 마커표시 함수, 현재 popup에 name이 들어가 있는데 index로 맵핑되게 for문을 돌렸으니까 index가 나올 것임
        
    seoul_map.save('./seoul_colleges.html')
    ````

- 팝업에 학교 이름 가로로 보이게 하기

  - ````python
    import pandas as pd
    import folium
    
    df = pd.read_excel('./서울지역 대학교 위치.xlsx')
    
    seoul_map = folium.Map(location=[37.55,126.98],tiles = 'Stamen Terrain',zoom_start=12)
    
    for name, lat, lng in zip(df.학교, df.위도, df.경도):
      # name을 학교로 설정
        iframe = folium.IFrame(name,width=300, height=100) 
        # iframe 프레임 객체 넓이 300, 높이 100으로 설정, IFrame은 UI 객체, 
        # popup으로 바로 들어갈 수 없기 때문에 popup을 객체로 변환하여 최종적으로 Marker에 들어갈 수 있게 설정하는 것임
        popup = folium.Popup(.) # popup이 바꾸면 
        folium.Marker([lat, lng], popup=popup).add_to(seoul_map) # popup=(popup)-> 이 친구를 똑같이 바꿔줘야함
    
    seoul_map
    ````

- 팝업 스타일 적용하기

  - ````python
    import pandas as pd
    import folium
    
    df = pd.read_excel('./서울지역 대학교 위치.xlsx')
    
    seoul_map = folium.Map(location=[37.55,126.98],tiles = 'Stamen Terrain',zoom_start = 12)
    
    for name, lat, lng in zip(df.학교, df.위도, df.경도):
        iframe = folium.IFrame(name, width=300,height= 100)
        popup = folium.Popup(iframe,max_width=600)
        folium.CircleMarker([lat,lng], # 마커에 스타일을 추가하는 코드
                      radius = 10, # 원의 반지름
                      color = 'brown', # 원의 둘레 색상
                      fill=True, 
                      fill_color='coral', # 원을 채우는 색
                      fill_opacity=0.7, # 투명도
                      popup=popup).add_to(seoul_map)
        
    seoul_map
    ````



## 5. 지도 영역에 단계구분도 표시하기

- ````python
  import pandas as pd
  import folium
  import json
  
  file_path = './경기도인구데이터.xlsx'
  df = pd.read_excel(file_path, index_col ='구분')
  df.columns = df.columns.map(str)
  
  geo_path = './경기도행정구역경계.json'
  try:
      geo_data = json.load(open(geo_path, encoding='utf-8'))
  except:
      geo_data = json.load(open(geo_path, encoding='utf-8-sig'))
  
  g_map = folium.Map(location=[37.5502,126.982],
                    tiles = 'Stamen Terrain', zoom_start=9)
  
  year = '2007'
  
  folium.Choropleth(geo_data=geo_data,
                   data = df[year],
                   colunms = [df.index, df[year]],
                  fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3, 
                   threshold_scale=[10000, 100000, 300000, 500000, 700000],
                   key_on = 'feature.properties.name',).add_to(g_map)
  
  g_map.save('./gyonggi_population_'+year+'.html')
  ````

- 