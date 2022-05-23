import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Data\Ask A Manager Salary Survey 2021 (Responses) - Form Responses 1.csv", index_col='Timestamp', parse_dates=['Timestamp'])
df.columns = ['edad', 'industria', 'trabajo', 'contexto trabajo', 'salario anual', 'bonos', 'moneda', 'otras monedas', 'contexto entrada', 'pais de trabajo', 'estado usa', 'ciudad usa', 'experiencia en total', 'experiencia en la industria', 'educacion', 'genero', 'raza']

df = df.drop(columns=['contexto trabajo', 'contexto entrada'])

df['bonos'] = df['bonos'].replace(np.nan, 0).astype(int)

df['salario anual'] = df['salario anual'].str.replace(",", "").astype(float)

df['pais de trabajo'] = df['pais de trabajo'].str.strip()


df['pais de trabajo'] = df['pais de trabajo'].replace(to_replace=r'\s', value=r'', regex=True)

df['pais de trabajo'] = df['pais de trabajo'].replace(to_replace=['England',
                                                                  'England,Gb',
                                                                  'England,UK',
                                                                  'England,UK.',
                                                                  'England,UnitedKingdom',
                                                                  'England/UK',
                                                                  'Englang',
                                                                  'ENGLAND',
                                                                  'GreatBritain',
                                                                  'U.K',
                                                                  'U.K.',
                                                                  'U.K.(northernEngland)',
                                                                  'UA',
                                                                  'UAE',
                                                                  'UK',
                                                                  'UK(England)',
                                                                  'UK(NorthernIreland)',
                                                                  'UK,butforgloballyfullyremotecompany',
                                                                  'UK,remote',
                                                                  'UKforU.S.company',
                                                                  'Uk',
                                                                  'UnitedKindom',
                                                                  'UnitedKingdom',
                                                                  'UnitedKingdom(England)',
                                                                  'UnitedKingdom.',
                                                                  'UnitedKingdomk',
                                                                  'Unitedkingdom',
                                                                  'Uniteskingdom',
                                                                  'uk',
                                                                  'unitedkingdom'], value='UK')

df['pais de trabajo'] = df['pais de trabajo'].replace(to_replace=['America',
                                                                  'TheUS',
                                                                  'TheUnitedStates',
                                                                  'U.S',
                                                                  'U.S.',
                                                                  'U.S.A',
                                                                  'U.S.A.',
                                                                  'U.S>',
                                                                  'U.SA',
                                                                  'U.s.',
                                                                  'U.s.a.',
                                                                  'UA',
                                                                  'UAE',
                                                                  'UNITEDSTATES',
                                                                  'UNitedStates',
                                                                  'US',
                                                                  'USA',
                                                                  'USA(companyisbasedinaUSterritory,Iworkremote)',
                                                                  "USA,butforforeigngov't",
                                                                  'USA--VirginIslands',
                                                                  'USAB',
                                                                  'USAtomorrow',
                                                                  'USD',
                                                                  'USS',
                                                                  'USaa',
                                                                  'USgovtemployeeoverseas,countrywithheld',
                                                                  'USofA',
                                                                  'UXZ',
                                                                  'UniitedStates',
                                                                  'UniteStates',
                                                                  'UnitedSTates',
                                                                  'UnitedSates',
                                                                  'UnitedSatesofAmerica',
                                                                  'UnitedStares',
                                                                  'UnitedState',
                                                                  'UnitedStatea',
                                                                  'UnitedStated',
                                                                  'UnitedStateds',
                                                                  'UnitedStatees',
                                                                  'UnitedStateofAmerica',
                                                                  'UnitedStates',
                                                                  'UnitedStates(IworkfromhomeandmyclientsareallovertheUS/Canada/PR',
                                                                  'UnitedStates-PuertoRico',
                                                                  'UnitedStatesOfAmerica',
                                                                  'UnitedStatesisAmerica',
                                                                  'UnitedStatesofAmerica',
                                                                  'UnitedStatesofAmerican',
                                                                  'UnitedStatesofAmericas',
                                                                  'UnitedStatesofamerica',
                                                                  'UnitedStatesp',
                                                                  'UnitedStatss',
                                                                  'UnitedStattes',
                                                                  'UnitedStatues',
                                                                  'UnitedStatus',
                                                                  'UnitedStatws',
                                                                  'UnitedSttes',
                                                                  'Unitedstates',
                                                                  'UnitedstatesofAmerica',
                                                                  'Unitedstatesofamerica',
                                                                  'Unitedstatew',
                                                                  'Unitedy',
                                                                  'UniteedStates',
                                                                  'UnitefStated',
                                                                  'UniterStatez',
                                                                  'UnitesStates',
                                                                  'Unitedstates',
                                                                  'UnitedstatesofAmerica',
                                                                  'Unitedstatesofamerica',
                                                                  'Unitedstatew',
                                                                  'Unitedy',
                                                                  'UniteedStates',
                                                                  'UnitefStated',
                                                                  'UniterStatez',
                                                                  'UnitesStates',
                                                                  'Us',
                                                                  'UsA',
                                                                  'Usa',
                                                                  'Usat',
                                                                  'u.s.',
                                                                  'uS',
                                                                  'uSA',
                                                                  'uk',
                                                                  'unitedStates',
                                                                  'unitedstated',
                                                                  'unitedstates',
                                                                  'unitedstatesofamerica',
                                                                  'us',
                                                                  'usa',
                                                                  'america',
                                                                  'Unitesstates',
                                                                  'UnitiedStates',
                                                                  'Uniyedstates',
                                                                  'UniyesStates',
                                                                  'UntedStates',
                                                                  'UntiedStates',
                                                                  'U.A.',
                                                                  "IworkforanUSbasedcompanybutI'mfromArgentina."], value='USA')

df['pais de trabajo'] = df['pais de trabajo'].replace(to_replace=['ARGENTINABUTMYORGISINTHAILAND',
                                                                  'Argentina',
                                                                  ], value='Argentina')

df['pais de trabajo'] = df['pais de trabajo'].replace(to_replace=['SouthAfrica',
                                                                  'Southafrica',
                                                                  'Africa'], value='Africa')

df['pais de trabajo'] = df['pais de trabajo'].replace(to_replace=['Australi',
                                                                  'Australia',
                                                                  'Australian',
                                                                  'australia'], value='Australia')

df1 = df.groupby('pais de trabajo')['salario anual'].median().astype(int).reset_index()
df2 = df1[df1['pais de trabajo'].isin(['USA', 'UK', 'Spain'])]
df2['real'] = None
print(df2)
print(df2.loc[133, 'real'])
plt.bar(data=df1[df1['pais de trabajo'].isin(['USA', 'UK', 'Spain'])],
        x='pais de trabajo',
        height='salario anual')
#plt.show()
for pais in df2['pais de trabajo']:
    for salario in df2['salario anual']:
        if pais == 'Spain':
            salario_real = (salario*1,12)
            df2.loc[133, 'real'] = salario_real
            
        if pais == 'UK':
            salario_real = (salario*1,26)
            df2.loc[145, 'real'] = salario_real
            
        if pais == 'USA':
            salario_real = salario
            df2.loc[146, 'real'] = salario_real
        
print(df2)