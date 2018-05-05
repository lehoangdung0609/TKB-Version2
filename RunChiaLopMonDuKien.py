import Data

#Chia Lop Mon Lien Thong o giai doan 1
def runClassficationLienThongGiaiDoan1():
    for i in Data.RETURN_GHICHU_LIENTHONG_GIAIDOAN_1_FROM_MON_TAM():
        GHICHU = i[0]
        # giai doan nay co co ENG siso > 40 nen bo qua viec kiem tra
        for j in Data.RETURN_ALL_FROM_MON_TAM_WHERE_MON_GHICHU_(GHICHU):
            MON_TAM, MON_TEN, MON_TINCHI, MON_GHICHU, MON_KHOANGANH, MON_NGANH, MON_CHUONGTRINH, MON_SISO, MON_LEC, MON_LAB, MON_LECLAB, MON_KHOA = j
            Data.INSERT_LOP_MON_DU_KIEN(MON_TAM,MON_GHICHU,'Liên Thông',1,1,1,MON_KHOANGANH,MON_SISO)
def runClassficationLienThongGiaiDoan2():
    for i in Data.RETURN_GHICHU_LIENTHONG_FROM_MON_TAM():
        GHICHU = i[0]
        checkEng = Data.CHECK_MON_GHICHU_CO_MA_ENG_IN_MON_TAM(GHICHU)
        if checkEng == 1:
            MaxSiso = Data.RETURN_MAX_SISO_FROM_MON_TAM_WHERE_MON_GHICHU(GHICHU)
            if MaxSiso > 40:
                LopKhoa = (MaxSiso // 40) +1
                print(LopKhoa,MaxSiso)
                for j in Data.RETURN_ALL_FROM_MON_TAM_WHERE_MON_GHICHU_(GHICHU):
                    MON_TAM, MON_TEN, MON_TINCHI, MON_GHICHU, MON_KHOANGANH, MON_NGANH, MON_CHUONGTRINH, MON_SISO, MON_LEC, MON_LAB, MON_LECLAB, MON_KHOA = j
                    MON_SISO = (int(MON_SISO) // LopKhoa) + 1
                    checkIn = Data.CHECK_MON_MA_IN_LOP_MON_DU_KIEN(MON_TAM,MON_GHICHU)
                    if checkIn == 0:
                        for l in range(LopKhoa):
                            Data.INSERT_LOP_MON_DU_KIEN(MON_TAM, MON_GHICHU+" "+str(l+1), 'Liên Thông', 2, 1, 1, MON_KHOANGANH, MON_SISO)
            elif MaxSiso <= 40:
                for j in Data.RETURN_ALL_FROM_MON_TAM_WHERE_MON_GHICHU_(GHICHU):
                    MON_TAM, MON_TEN, MON_TINCHI, MON_GHICHU, MON_KHOANGANH, MON_NGANH, MON_CHUONGTRINH, MON_SISO, MON_LEC, MON_LAB, MON_LECLAB, MON_KHOA = j
                    checkIn = Data.CHECK_MON_MA_IN_LOP_MON_DU_KIEN(MON_TAM,MON_GHICHU)
                    if checkIn == 0:
                            Data.INSERT_LOP_MON_DU_KIEN(MON_TAM, MON_GHICHU, 'Liên Thông', 2, 1, 1, MON_KHOANGANH, MON_SISO)


runClassficationLienThongGiaiDoan2()