import pandas as pd

# 파일 경로
file_path = '/Users/kangminjung/text to excel/기업 홈페이지.txt'

# 텍스트 파일 읽기
with open(file_path, 'r', encoding='euc-kr') as file:  # 인코딩을 euc-kr로 변경
    lines = file.readlines()

# 데이터 프레임 생성
data = []
for line in lines:
    if '-' in line:
        name, url = line.split(' - ')
        url = url.strip()
        data.append([name, url])

df = pd.DataFrame(data, columns=['기관', 'URL'])

# 엑셀 파일로 저장
excel_path = '/Users/kangminjung/text to excel/기업 홈페이지_엑셀.xlsx'
df.to_excel(excel_path, index=False)

print(f"엑셀 파일이 성공적으로 저장되었습니다: {excel_path}")
