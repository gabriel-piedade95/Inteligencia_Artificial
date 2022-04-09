import matplotlib.pyplot as plt

def abre_arquivo(file_path):

    dados = []
    with open('iris.data', 'r', encoding='utf-8') as f:

        for linha in f:

            linha = linha.split(',')
        
            vetor = [float(x) for x in linha[:4]]
            vetor.append(linha[4].strip('\n'))
            dados.append(vetor)

    return dados


def plot_reta(X, Y, w, b):
  
  fig = plt.figure(figsize=(10,8))
  x1 = [x[0] for x in X]

  m = -w[0]/w[1]
  c = -b/w[1]
  x2 = [x*m + c for x in x1]

  classe1 = []
  classe2 = []

  for i in range(len(Y)):
    if Y[i] == -1:
      classe1.append(X[i])
    else:
      classe2.append(X[i])


  plt.scatter([x[0] for x in classe1], [x[1] for x in classe1],marker='x')
  plt.scatter([x[0] for x in classe2], [x[1] for x in classe2],marker='o')
  plt.xlabel("feature 1")
  plt.ylabel("feature 2")
  plt.plot(x1, x2, 'y-')

