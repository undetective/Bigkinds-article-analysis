rdata=open("Rawdata.csv","r")
line=rdata.readline()
result=[]
rawdata=[]

# 기사 데이터 - 국가 데이터 결합
for line in rdata:
    line=line.strip()
    lines=line.split(",",2)  # ["일자","언론사","제목"]
    rawdata.append(lines)

    # 국가 데이터 분할 (커서 초기화 위해 중간 삽입)
    ndata = open("국가명.csv", "r")
    line = ndata.readline()
    nations = []

    # 국가명 리스트화 (@nations)
    for line2 in ndata:
        line2=line2.strip()
        lines2=line2.split(" // ")
        nations.append(lines2)

    # 기사 제목과 국가명 합치기 (@result)
    for i in range(len(nations)):
        comb=[]
        for n in range(len(nations[i])):
            if nations[i][n] in lines[2]:
                comb.append(lines)
                comb.append(nations[i])
                result.append(comb)

    # 인도/인도네시아 구분
    for exception in result:
        if "인도네시아" in exception[0][2]:
            if exception[1][0] == "인도":
                result.remove(exception)
    # 리비아/볼리비아 구분
    for exception in result:
        if "볼리비아" in exception[0][2]:
            if exception[1][0] == "리비아":
                result.remove(exception)
ndata.close()
rdata.close()


# 국가별, 연도별 기사 수 csv 파일 생성

ndata=open("국가명.csv","r")
outfile=open("국가별_연도별_기사.csv","w")
outfile.write("국가명,2015,2016,2017,2018,계\n")
line=ndata.readline()
natdata=[]

for line in ndata:
    line=line.strip()
    lines=line.split(" // ")
    natdata.append(lines)

    adata=open("RawData.csv","r")
    line=adata.readline()
    articles=[]
    y2015 = []
    y2016 = []
    y2017 = []
    y2018 = []

    for line2 in adata:
        line2=line2.strip()
        lines2=line2.split(",",2)
        articles.append(lines2)

    for article in articles:
        for i in range(len(lines)):
            if lines[0] == "인도":
                if "인도네시아" in article[2]:
                    continue
            if lines[i] in article[2]:
                if "2015" in article[0]:
                    y2015.append(article)
                elif "2016" in article[0]:
                    y2016.append(article)
                elif "2017" in article[0]:
                    y2017.append(article)
                elif "2018" in article[0]:
                    y2018.append(article)
    total=len(y2015)+len(y2016)+len(y2017)+len(y2018)
    outfile.write(lines[0]+",%d,%d,%d,%d,%d\n" %(len(y2015),len(y2016),len(y2017),len(y2018),total))
    adata.close()
ndata.close()
outfile.close()

print(""""국가별_연도별_기사.csv" 파일이 생성되었습니다.\n\n"""+"-"*60+"\n")

# 시작화면
print("원하는 검색 서비스를 골라주세요")
print("1. 기사제목에 나타난 국가명을 대상으로, 연도별 각 국가와 관련된 기사 수 검색")
print("2. 언론사명과 국가명을 입력하면 작성한 기사의 개수 검색")

# 과제 1. 기사제목에 나타난 국가명을 대상으로, 연도별 각 국가와 관련된 기사 수 검색
while True:
    service = input("서비스 선택(1, 2 / 종료시 엔터): ")
    if service == "":
        break
    if int(service) == 1:
        print("\n===================연도별/국가별 한류 기사 검색===================\n")
        year=input("연도를 입력해주세요(2015-2018): ")
        nation=input("국가를 입력해주세요: ")
        searchResult=[]
        year=year.strip()
        nation=nation.strip()

        for i in range(len(result)):
            if year in result[i][0][0]:     # 연도 필터링
                for j in range(len(result[i][1])):
                    if nation == result[i][1][j]:  # 국가 필터링
                        searchResult.append(result[i])

        print(year,"년 제목에",nation,"이(가) 포함된 한류 관련 기사는 %d건 입니다." %(len(searchResult)))
        print("\n===================검색 결과===================\n")
        for i in range(len(searchResult)):
            print(searchResult[i])

    # 과제 2. 언론사명과 국가명을 입력하면 작성한 기사의 개수 검색
    if int(service) == 2:
        print("===================언론사/국가별 한류 기사 검색===================")
        media=input("언론사명을 입력해주세요(e.g. 중앙일보): ")
        nation2=input("국가를 입력해주세요: ")
        searchResult2=[]
        media=media.strip()
        nation2=nation2.strip()

        for i in range(len(result)):
            if media in result[i][0][1]: # 언론사 필터링
                for j in range(len(result[i][1])):
                    if nation2 == result[i][1][j]:  # 국가 필터링
                        searchResult2.append(result[i])
        print(media,"언론사에서 작성한 ",nation2,"의 한류 관련 기사는 %d건 입니다. (2015-2018년 기준)" %(len(searchResult2)))
        print("\n===================검색 결과===================\n")
        for i in range(len(searchResult2)):
            print(searchResult2[i])
    print("\n"+"="*60+"\n")
    print("기사 데이터 출처: 빅카인즈(https://www.kinds.or.kr/) 2015-2018년 한류 관련 뉴스기사")
    print("국가 데이터 출처: 국립국어원 국가명한글표기기준안\n")

rdata.close()

