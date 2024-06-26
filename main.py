import requests
import pandas as pd
import matplotlib.pyplot as plt
def main():
    url = 'http://api.meteored.cl/index.php?api_lang=cl&localidad=18578&affiliate_id=59lbfhamrp71&v=3.0'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['day'])
    df = df.transpose()
    df = df[['name','tempmin','tempmax']]
    print(df)

    df['tempmin'] = df['tempmin'].astype(float)
    df['tempmax'] = df['tempmax'].astype(float)

    dff =df.plot(x='name', y=['tempmin','tempmax'], kind='bar', colormap='coolwarm')
    plt.title('Temperaturas de 5 días en Santiago')
    plt.ylabel('Temperatura')
    plt.xlabel('Días')
    plt.legend(['Mínima','Máxima'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    for p in dff.patches:
        dff.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.savefig('grafico.png')
if __name__ == "__main__":
    main()
