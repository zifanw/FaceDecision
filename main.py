import numpy as np

# Accuracy: (m, c, i)
# Processing: (m) 
# Resource: (m) =CPU+memory (megabytes)
n_model = 6
n_remote = 4
n_sigma = 3
n_face_interval = 4

# np.load('/tmp/123.npy')
data = np.load('data.npz')

ModelAccuracy = data['mAP'] #np.random.rand(n_model, n_face_interval, n_sigma)

ModelProcessing = data['latency'] # np.random.rand(n_model)

ModelResource = data['resource']# np.random.rand(n_model,2) # GPU, CPU

# print 'accuracy: ', ModelAccuracy
# print 'latency: ', ModelProcessing
# print 'resource: ', ModelResource

weight = 0.3
resolution = 224*224*3*8
CPU_threshold = 1024 # CPU + memory
GPU_threshold = 1024 # GPU
# 2G: 21.4kbps; 3G: 384kbps; 4G: 50Mbps
bw = [21400/8,384000/8,50e6/8]
def decision(bandwidth=2, latency=1, sigma=0,n_face_interval=0, weight=0.1, energy=1, resource=1): 
    # print bandwidth,latency
    '''
    model, accuracy
    remote: model 0
    '''
    max_utility = 0
    model_acc = 0
    model = -1
    for i in range(n_model):
        sigma = bandwidth
        processing = ModelProcessing[i]
        
        speed = np.random.randn()*1000+float(bw[bandwidth]) 
        print('sp;;',speed)
        transmission = resolution/speed if i>=n_remote else 0
        total_latency = weight * (processing + transmission + latency)
        if i<n_remote: # local model use sigma=0
            accuracy = ModelAccuracy[i][0][n_face_interval]
        else:
            accuracy = ModelAccuracy[i][sigma][n_face_interval]
        
        utility = accuracy - total_latency
        print('Model %i |UTL: %f| ACC: %f|LTC: %f|PRO: %f|TRM: %f' %(i, utility, accuracy, total_latency, processing,transmission))
        if utility>max_utility:  
            # if using local model: discard model not satisfying constraints
            if i < n_remote and (ModelResource[i][1]>GPU_threshold or ModelResource[i][0]>CPU_threshold or processing>energy):
                continue
            
            model = i 
            max_utility = utility
            model_acc = accuracy
    return model, model_acc

print decision()

# def acc_exp():
#     latency = []