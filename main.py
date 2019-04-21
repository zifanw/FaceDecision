import numpy as np

# Accuracy: (m, c, i)
# Processing: (m) 
# Resource: (m) =CPU+memory (megabytes)
n_model = 3
n_sigma = 3
n_face_interval = 3

# np.load('/tmp/123.npy')
ModelAccuracy = np.random.rand(n_model, n_sigma, n_face_interval)

ModelProcessing = np.random.rand(n_model)

ModelResource = np.random.rand(n_model)

# print 'accuracy: ', ModelAccuracy
# print 'latency: ', ModelProcessing
# print 'resource: ', ModelResource

weight = 0.3
resolution = 224*224
resource_threshold = 300 # CPU + memory

def decision(bandwidth=100000.0, latency=1, sigma=0,n_face_interval=2, weight=0.03, energy=1, resource=1): 
    print bandwidth,latency
    '''
    model, accuracy
    remote: model 0
    '''
    max_utility = 0
    model_acc = 0
    model = -1
    for i in range(n_model):
        processing = ModelProcessing[i]
        transmission = resolution/bandwidth if i==0 else 0
        total_latency = weight * (processing + transmission + latency)
        if i!=0:
            accuracy = ModelAccuracy[i][n_face_interval][sigma]
        else:
            accuracy = max([ModelAccuracy[i][n_face_interval][s] for s in range(n_sigma)])
        utility = accuracy - total_latency
        print 'Model %i |UTL: %f| ACC: %f|LTC: %f|PRO: %f|TRM: %f' %(i, utility, accuracy, total_latency, processing,transmission)
        if utility>max_utility:  
            # if using local model: check constraints
            if i!=0 and (ModelResource[i]>resource_threshold or processing>energy):
                continue
            
            model = i 
            max_utility = utility
            model_acc = accuracy
    return model, model_acc

# print decision()

# def acc_exp():
#     latency = []