import numpy as np

# Accuracy: (m, c, i)
# Processing: (m) 
# Resource: (m) =CPU+memory (megabytes)
n_model = 3
n_compress_rate = 5
n_face_interval = 3

# np.load('/tmp/123.npy')
ModelAccuracy = np.random.rand(n_model, n_compress_rate, n_face_interval)

ModelProcessing = np.random.rand(n_model)

ModelResource = np.random.rand(n_model)

# print 'accuracy: ', ModelAccuracy
# print 'latency: ', ModelProcessing
# print 'resource: ', ModelResource

weight = 0.3
resolution = 224*224
resource_threshold = 300 # CPU + memory

def decision(bandwidth=100000.0, latency=1, compress_rate=3,n_face_interval=2, weight=0.03, energy=1, resource=1): 
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
        accuracy = ModelAccuracy[i][compress_rate][n_face_interval]
        utility = accuracy - total_latency
        # print i,utility
        print 'Model %i |UTL: %f| ACC: %f|LTC: %f|PRO: %f|TRM: %f' %(i, utility, accuracy, total_latency, processing,transmission)
        if utility>max_utility:
            
            if i!=0 and (ModelResource[i]>resource_threshold or processing>energy):
                continue
            
            model = i 
            max_utility = utility
            model_acc = accuracy
    return model, model_acc

# print decision()

# def acc_exp():
#     latency = []