import pickle

def load_gp_model(name_file):

	f =  open(name_file, 'rb')
	est = pickle.load(f)
	return est

est = load_gp_model('est_gp_model.pkl')

print(est._program,'\n')

print('predict: ',est.predict([[0, 0, 0, 0, 0, 0, 0, 0, 0]]))
print('predict: ',est.predict([[-1, -1, 1, 1, -1, 1, -1, 1, -1]]))
print('predict: ',est.predict([[-1, -1, 1, 1, -1, 0, -1, 1, 0]]))