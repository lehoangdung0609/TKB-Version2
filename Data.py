import Connection
cursor = Connection.connectDTU() # nhớ close connection
#Insert đặt tên : insert + tên bảng
def INSERT_LOP_MON_DU_KIEN(MON_MA,LOP_MON_GHICHU,KHOI, GIAI_DOAN, HOC_KI, NAM_HOC,KHOA_NGANH,LOP_MON_SISO):
    check = CHECK_MON_MA_IN_LOP_MON_DU_KIEN(MON_MA,LOP_MON_GHICHU)
    if check == 1:
        print("Exist")
    elif check == 0:
        sql = ("INSERT  INTO LOP_MON_DU_KIEN (MON_MA,LOP_MON_GHICHU,KHOI, GIAI_DOAN, HOC_KI, NAM_HOC,KHOA_NGANH,LOP_MON_SISO)\
                VALUES(N'{A}', N'{B}', N'{C}', {D}, {E},{F}, N'{G}', {H}) \
             ").format(A = MON_MA, B=LOP_MON_GHICHU, C= KHOI, D= GIAI_DOAN, E=HOC_KI, F=NAM_HOC, G=KHOA_NGANH, H=LOP_MON_SISO)
        print(sql)
        cursor.execute(sql)
        cursor.commit()
def INSERT_MON_TAM(MON_TAM,MON_TEN,MON_TINCHI,MON_GHICHU,MON_KHOANGANH,MON_NGANH,MON_CHUONGTRINH,MON_SISO,MON_LEC,MON_LAB,MON_LECLAB ,MON_KHOA):
    sql = ("INSERT INTO [dbo].[MON_TAM]\
     VALUES\
           (N'{0}'\
           ,N'{1}'\
           ,{2}\
           ,N'{3}'\
           ,N'{4}'\
           ,N'{5}'\
           ,N'{6}'\
           ,{7}\
           ,N'{8}'\
           ,N'{9}'\
           ,N'{10}',N'{11}')").format(MON_TAM,MON_TEN,MON_TINCHI,MON_GHICHU,MON_KHOANGANH,MON_NGANH,MON_CHUONGTRINH,MON_SISO,MON_LEC,MON_LAB,MON_LECLAB ,MON_KHOA)
    cursor.execute(sql)
    cursor.commit()
def insertMonLoai(mon_ma,ghichu,loaihoctap,tinchi,tiettuan):
    check = checkInMONLOAIHT(mon_ma,ghichu,loaihoctap)
    if check == 0:
        print("Exits")
        print(mon_ma,ghichu,loaihoctap,tinchi,tiettuan)
    elif check == 1:
        sql = ("INSERT INTO [dbo].[MON_LOAI_HOC_TAP]\
     VALUES\
           (N'{0}'\
           ,N'{1}'\
           ,N'{2}'\
           ,{3}\
           ,{4})").format(mon_ma,ghichu,loaihoctap,tinchi,tiettuan)
        cursor.execute(sql)
        cursor.commit()
def insertLOPMONKHONGXEP():
    sql = ("select * from MON_LOAI_HOC_TAP")
    for i in cursor.execute(sql).fetchall():
        check = checkCourseNotInTime(i[0])
        if check == 1:
           pass
        elif check == 0:
            if i[2] == 'LEC':
                pass
            elif i[2]== 'LAB':
                sql =("INSERT INTO [dbo].[LOP_MON_KHONG_XEP]\
         VALUES\
               (N'{0}'\
               ,N'{1}'\
               ,N'{2}')").format(i[0],i[1],i[2])
                print(sql)
                cursor.execute(sql)
                cursor.commit()
#Select trả về danh sách đặt tên return + dữ liệu trả về + FROM + TEN BANG + WHERE + DIEUKIEN ( * = All )
def RETURN_ALL_FROM_LOP_MON_DU_KIEN_WHERE_KHOI(group):
    sql = ("select * from LOP_MON_DU_KIEN where KHOI = N'{0}'").format(group)
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
    cursor.close()
def RETURN_ALL_FROM_MON_TAM():
    sql =("select * from MON_TAM")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
def RETURN_ALL_UUTIEN_FROM_MON_TAM():
    sql =("  SELECT * \
  FROM [TKB_VERSION2].[dbo].[MON_TAM]\
  WHERE (MON_GHICHU like N'%CSU%' or MON_GHICHU like N'%PSU%' or MON_GHICHU like N'%CMU%' or MON_GHICHU like N'%PNU%' ) and MON_KHOANGANH != ''\
  order by MON_NGANH , MON_KHOANGANH")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
def RETURN_ALL_LIENTHONG_GIAIDOAN_1_FROM_MON_TAM():
    sql = ("select * from MON_TAM where MON_CHUONGTRINH = N'Liên Thông' and MON_KHOA not in (N'Khoa Dược',N'Khoa Kiến Trúc') ")
    A = []
    for i in cursor.execute(sql).fetchall():
        a = i[3]
        if a[0:3] == 'D22' and a[-1] == 'B':
            A.append(i)
    for i in RETURN_ALL_LIENTHONG_GIAIDOAN_1_PHAN_2_FROM_MON_TAM():
        A.append(i)
    return A
def RETURN_ALL_LIENTHONG_GIAIDOAN_1_PHAN_2_FROM_MON_TAM():
    sql = ("select * from MON_TAM where MON_CHUONGTRINH = N'Liên Thông' and MON_GHICHU in ('T22YDD A', 'T22KDN A','D21YDH A-B', 'D21YDH B-B', 'T20YDH A-B ')")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
def RETURN_ALL_LIENTHONG_FROM_MON_TAM():
    sql = ("select * from MON_TAM where MON_CHUONGTRINH = N'Liên Thông'")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
def RETURN_ALL_DAICUONG_FROM_MON_TAM():
    sql =("select * from MON_TAM where MON_CHUONGTRINH != N'Liên Thông'")
    A = []
    for i in cursor.execute(sql).fetchall():
        a = checkCourse.checkSection(i[0])
        if a == 5:
            A.append(i)
    return A
def RETURN_ALL_DAICUONGNGANH_FROM_MON_TAM():
    sql = ("select * from MON_TAM where MON_CHUONGTRINH != N'Liên Thông'")
    A = []
    for i in cursor.execute(sql).fetchall():
        a = checkCourse.checkSection(i[0])
        if a == 2:
            A.append(i)
    return A
def RETURN_ALL_CHUYENNGANH_FROM_MON_TAM():
    sql = ("SELECT * \
  FROM [TKB_VERSION2].[dbo].[MON_TAM]\
  WHERE MON_TAm in ( SELECT COURSE_NUMBER FROM tkb_COURSE_IN_SECTION where SECTION = N'Chuyên Ngành') and MON_CHUONGTRINH = N'Chính Quy'\
  ")
    A = []
    for i in cursor.execute(sql).fetchall():
       A.append(i)
    return A
def RETURN_ALL_CHUYENNGANH_SISO_45_FROM_MON_TAM():
    sql = ("SELECT DISTINCT \
      [MON_GHICHU] \
    FROM [TKB_VERSION2].[dbo].[MON_TAM] \
WHERE MON_TAM in ( SELECT COURSE_NUMBER FROM tkb_COURSE_IN_SECTION where SECTION = N'Chuyên Ngành') and MON_CHUONGTRINH = N'Chính Quy' \
and  ([MON_TAM] like 'CSU%' or [MON_TAM] like 'CMU%' or [MON_TAM] like 'PSU%' or [MON_TAM] like 'PNU%')\
  ")
    A = []
    for i in cursor.execute(sql).fetchall():
       A.append(i)
    return A
    cursor.close()
def RETURN_ALL_FROM_MON_TAM_WHERE_MON_GHICHU_(course_note):
    sql =("SELECT * \
  FROM [TKB_VERSION2].[dbo].[MON_TAM] WHERE MON_GHICHU =N'{0}'").format(course_note)
    A =[]
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
    cursor.close
def RETURN_COUNT_INSTRUCTOR_ID_NUMBER_FROM_TKB_INSTRUCTOR_COURSE_WHERE_COURSE_NUMBER(course_number):
    sql =("SELECT [COURSE_NUMBER]\
      ,count([INSTRUCTOR_ID_NUMBER])\
  FROM [TKB_VERSION2].[dbo].[tkb_INSTRUCTOR_COURSE] WHERE COURSE_NUMBER =N'{0}'\
  group by [COURSE_NUMBER] order by COURSE_NUMBER").format(course_number)
    check = cursor.execute(sql).fetchone()[1]
    if check == 0:
        return 0
    elif check > 0:
        return check
    cursor.close()
def RETURN_ALL_MON_GHICHU_UUTIEN_FROM_MON_TAM():
    sql =("SELECT DISTINCT \
      [MON_GHICHU]\
  FROM [TKB_VERSION2].[dbo].[MON_TAM] WHERE MON_CHUONGTRINH=N'Chính Quy' and\
  MON_TAM in (select COURSE_NUMBER from tkb_QUANTITY_OF_COURSE) and MON_NGANH !=''")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
    cursor.close()
def RETURN_ALL_SECTION_FROM_tkb_COURSE_IN_SECTION_WHERE_COURSE_NUMBER(course_number):
    sql = ("SELECT SECTION \
  FROM [tkb_COURSE_IN_SECTION] \
  WHERE COURSE_NUMBER = '{0}'").format(course_number)
    a = cursor.execute(sql).fetchone()[0]
    if a == 'GIÁO DỤC THỂ CHẤT & QUỐC PHÒNG':
        return 1
    elif a == 'ĐẠI CƯƠNG NGÀNH':
        return 'Đại Cương Ngành'
    elif a == 'CHUYÊN NGÀNH':
        return 'Chuyên Ngành'
    elif a is None:
        return 4
    elif a == 'ĐẠI CƯƠNG':
        return 'Đại Cương'
    cursor.close()
def RETURN_ALL_FROM_LOP_MON_DU_KIEN():
    sql =("select * from [LOP_MON_DU_KIEN]")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
    cursor.close()
def RETURN_LEC_LAB_LECLAB_FROM_MON_TAM_WHERE_MON_TAM(course_number):
    sql=("select DISTINCT MON_LEC , MON_LAB, MON_LECLAB from MON_TAM where MON_TAM = N'{0}'").format(course_number)
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
    cursor.close()
def RETURN_ALL_LEC_FROM_MON_LOAI_HOC_TAP():
    sql = ("SELECT a.* FROM [MON_LOAI_HOC_TAP] a LEFT JOIN LOP_MON_KHONG_XEP b ON b.LOAI_HOC_TAP = a.LOAI_HOC_TAP and b.MON_MA = a.MON_MA WHERE a.MON_MA not in ( 'CS 201','CS 101') AND b.LOAI_HOC_TAP is null and b.MON_MA is null order by MON_LOAI_HOC_TIETTUAN DESC")
    A = []
    for i in cursor.execute(sql).fetchall():
        if i[2] == 'LEC':
            A.append(i)
        elif i[2] == 'LAB':
            check = checkIsLEC(i[0])
            if check == 1:
                if i[0] == 'PHM 402' and i[0] == 'PHM 407' and  i[0] == 'CMU-SE 403' :
                    A.append(i)
    return A
def RETURN_ALL_LEC_LIENTHONG_FROM_MON_LOAI_HOC_TAP():
    sql = ("SELECT a.* FROM [MON_LOAI_HOC_TAP] a LEFT JOIN LOP_MON_KHONG_XEP b ON b.LOAI_HOC_TAP = a.LOAI_HOC_TAP and b.MON_MA = a.MON_MA WHERE a.MON_MA not in ( 'CS 201','CS 101') AND b.LOAI_HOC_TAP is null and b.MON_MA is null order by MON_LOAI_HOC_TIETTUAN DESC")
    A = []
    for i in cursor.execute(sql).fetchall():
        ghichu = i[1]
        if ghichu[0] =='D' or ghichu[0] =='T':
            if i[2] == 'LEC':
                A.append(i)
            elif i[2] == 'LAB':
                check = checkIsLEC(i[0])
                if check == 1:
                    if i[0] == 'PHM 402' and i[0] == 'PHM 407' and  i[0] == 'CMU-SE 403' :
                        A.append(i)
    return A
    cursor.close()
def RETURN_GIAI_DOAN_LOP_MON_SISO_FROM_LOP_MON_DU_KIENreturnCourseInLopMonDuKien(mon,ghichu):
    sql =("select giai_doan , LOP_MON_SISO from LOP_MON_DU_KIEN where MON_MA =N'{0}' and LOP_MON_GHICHU =N'{1}'").format(mon,ghichu)
    result = cursor.execute(sql).fetchone()
    return result[0],result[1]
    cursor.close()
def RETURN_GHICHU_LIENTHONG_GIAIDOAN_1_FROM_MON_TAM():
    sql = ("select DISTINCT MON_GHICHU from MON_TAM where MON_CHUONGTRINH = N'Liên Thông' and MON_KHOA not in (N'Khoa Dược',N'Khoa Kiến Trúc') ")
    A = []
    for i in cursor.execute(sql).fetchall():
        a = i[0]
        if a[0:3] == 'D22' and a[-1] == 'B':
            A.append(i)
    for i in RETURN_GHICHU_LIENTHONG_GIAIDOAN_1_PHAN_2_FROM_MON_TAM():
        A.append(i)
    return A
def RETURN_GHICHU_LIENTHONG_GIAIDOAN_1_PHAN_2_FROM_MON_TAM():
    sql = ("select DISTINCT MON_GHICHU from MON_TAM where MON_CHUONGTRINH = N'Liên Thông' and MON_GHICHU in ('T22YDD A', 'T22KDN A','D21YDH A-B', 'D21YDH B-B', 'T20YDH A-B ')")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
def RETURN_MAX_SISO_FROM_MON_TAM_WHERE_MON_GHICHU(MON_GHICHU):
    sql =("SELECT max([MON_SISO]) FROM [TKB_VERSION2].[dbo].[MON_TAM] WHERE MON_GHICHU = N'{0}'").format(MON_GHICHU)
    return cursor.execute(sql).fetchone()[0]
def RETURN_GHICHU_LIENTHONG_FROM_MON_TAM():
    sql = ("select DISTINCT MON_GHICHU from MON_TAM where MON_CHUONGTRINH = N'Liên Thông'")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A
def RETURN_GHICHU_LIENTHONG_GIAIDOAN_2_FROM_MON_TAM():
    sql = ("select DISTINCT a.MON_GHICHU from MON_TAM a left join LOP_MON_DU_KIEN b ON b.MON_MA = a.MON_TAM and b.LOP_MON_GHICHU = a.MON_GHICHU and b.MON_MA is null and b.LOP_MON_GHICHU is null  where MON_CHUONGTRINH = N'Liên Thông'")
    A = []
    for i in cursor.execute(sql).fetchall():
        A.append(i)
    return A





#select để kiểm tra tồn tại check + điều kiện + In + tên bảng
def CHECK_MON__MA_IN_MON(course_number):
    sql =("select count(*) from MON where mon_ma = N'{0}'").format(course_number)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 1
    elif check == 1:
        return 0
    cursor.close()
def CHECK_MON_MA_IN_LOP_MON_DU_KIEN(course_number,course_note):
    sql =("select count(*) from LOP_MON_DU_KIEN where mon_ma = N'{0}' and LOP_MON_GHICHU =N'{1}'").format(course_number,course_note)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 0
    elif check > 0:
        return 1
    cursor.close()
def CHECK_MON_TAM_MON_GHI_CHU_MON_KHOANGANH_MON_NGANH_MON_KHOA_IN_MON_TAM(MON_TAM,MON_GHICHU,MON_KHOANGANH,MON_NGANH,MON_KHOA):
    sql = ("SELECT count(*) FROM MON_TAM where [MON_TAM] =N'{0}' \
      and [MON_GHICHU]=N'{1}' \
      and [MON_KHOANGANH]=N'{2}' \
      and [MON_NGANH]=N'{3}' \
      and[MON_KHOA]=N'{4}'").format(MON_TAM,MON_GHICHU,MON_KHOANGANH,MON_NGANH,MON_KHOA)
    count = cursor.execute(sql).fetchone()[0]
    if count == 0:
        return 1
    elif count == 1:
        return 0
    cursor.close()
def CHECK_MON_GHICHU_CO_MA_ENG_IN_MON_TAM(note):
    sql =("SELECT count(*) FROM [TKB_VERSION2].[dbo].[MON_TAM] WHERE MON_GHICHU =N'{0}' and MON_TAM like 'ENG%'").format(note)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 0
    elif check > 0:
        return 1
    cursor.close()
def CHECK_MON_GHICHU_CO_MA_UUTIEN_IN_MON_TAM(note):
    sql =("SELECT count(*) FROM [TKB_VERSION2].[dbo].[MON_TAM] WHERE MON_GHICHU =N'{0}' and ( MON_TAM like 'CSU%' or  MON_TAM like 'CMU%' or  MON_TAM like 'PSU%' or  MON_TAM like 'PNU%')").format(note)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 0
    elif check > 0:
        return 1
    cursor.close()
def CHECK_MON_MA_MON_GHICHU_LOAI_HOC_TAP_IN_MON_LOAI_HOC_TAP(mon_ma,ghichu, loai):
    sql =("select count(*) from MON_LOAI_HOC_TAP where MON_MA =N'{0}' and LOP_MON_GHICHU =N'{1}' and LOAI_HOC_TAP ='{2}'").format(mon_ma,ghichu,loai)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 1
    elif check > 0:
        return 0
    cursor.close
def checkCourseNotInTime(course_number):
    sql=("SELECT count(*)\
  FROM [tkb_COURSE_NOT_IN_TIMETABLE] WHERE COURSE_NUMBER =N'{0}'").format(course_number)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 1
    elif check > 0:
        return 0
def checkIsLEC(course_number):
    sql = ("select count(*) from [tkb_COURSE_IN_FACILITY] WHERE COURSE_NUMBER = N'{0}' ").format(course_number)
    check = cursor.execute(sql).fetchone()[0]
    if check == 0:
        return 1
    elif check > 0:
        return 0

#Update  đặt tên updtae + dữ liệu thay đổi + tên bảng




#Delet đặt tên Del + diều kiện + tên bảng
