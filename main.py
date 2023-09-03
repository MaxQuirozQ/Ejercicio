
import pickle

# cargo el modelo
#filename = 'modeloentrenado.pkl'
filename = input("Ingrese nombre del archivo donde está guardado el modelo entrenado: ")
loaded_model = pickle.load(open(filename, 'rb'))

# cargo el normalizador
filename_norm_train = 'normalizadorentrenado_train.pkl'
filename_norm_val = 'normalizadorentrenado_val.pkl'
filename_norm_test = 'normalizadorentrenado_test.pkl'

with open(filename_norm_train,'rb') as f:
    sc_train = pickle.load(f)
with open(filename_norm_val,'rb') as f:
    sc_val = pickle.load(f)
with open(filename_norm_test,'rb') as f:
    sc_test = pickle.load(f)