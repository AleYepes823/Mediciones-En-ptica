import pandas as pd
import uncertainties as unc
import uncertainties.unumpy as unp

def LecturaTitulos(Ruta):
    Data = pd.read_excel(f'{Ruta}/ResultadosTitulo.xlsx',index_col=0,converters = {'DistOb':unc.ufloat_fromstr,'DistIm':unc.ufloat_fromstr,'DistFo':unc.ufloat_fromstr})
    TOCSV = {}
    for nombre in Data.index:
        TOCSV[nombre] = {'DistOb':unp.nominal_values(Data['DistOb'][nombre]),'dDistOb':unp.std_devs(Data['DistOb'][nombre]),
                        'DistIm':unp.nominal_values(Data['DistIm'][nombre]),'dDistIm':unp.std_devs(Data['DistIm'][nombre]),
                        'DistFo':unp.nominal_values(Data['DistFo'][nombre]),'dDistFo':unp.std_devs(Data['DistFo'][nombre])}
    TOCSV = pd.DataFrame(TOCSV).T
    TOCSV = TOCSV.astype(float)
    print(TOCSV['DistFo'].mean(),TOCSV['DistFo'].std())
    foco = unc.ufloat(TOCSV['DistFo'].mean(),TOCSV['DistFo'].std())
    TOCSV.to_csv(f'{Ruta}/ResultadosTitulo.csv',float_format = '%.2f',index = False)
    return Data, foco

def LecturaImagenes(Ruta):
    Data = pd.read_excel(f'{Ruta}/ResultadosImagenes.xlsx',index_col=0,converters = {'n':int,'dist':unc.ufloat_fromstr,'mag':unc.ufloat_fromstr,'foco':unc.ufloat_fromstr})
    Data2, foco2 = LecturaTitulos(Ruta)
    Data['DistIm'] = Data2['DistIm']
    TOCSV = {}
    for nombre in Data.index:
        TOCSV[nombre] = {'DistIm':unp.nominal_values(Data['DistIm'][nombre]),'dDistIm':unp.std_devs(Data['DistIm'][nombre]),
                        'dist':unp.nominal_values(Data['dist'][nombre]),'ddist':unp.std_devs(Data['dist'][nombre]),
                        'mag':unp.nominal_values(Data['mag'][nombre]),'dmag':unp.std_devs(Data['mag'][nombre]),
                        'foco':unp.nominal_values(Data['foco'][nombre]),'dfoco':unp.std_devs(Data['foco'][nombre])}
    TOCSV = pd.DataFrame(TOCSV).T
    TOCSV = TOCSV.astype(float)
    TOCSV['n'] = Data['n']
    TOCSV.to_csv(f'{Ruta}/ResultadosImagen.csv',float_format = '%.2f',index = False)
    foco = unc.ufloat(TOCSV['foco'].mean(),TOCSV['foco'].std())
    print(TOCSV['foco'].mean(),TOCSV['foco'].std(),(foco-foco2)*100/foco)
    ...
LecturaImagenes('ImagenLab/datos')