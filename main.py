import numpy as np

# Accuracy: (m, c, i)
# Processing: (m) 
# Resource: (m) =CPU+memory (megabytes)

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

# weight = 0.3
resolution = 224*224*3*8
CPU_threshold = 1024 # CPU + memory
GPU_threshold = 1024 # GPU
# 2G: 21.4kbps; 3G: 384kbps; 4G: 50Mbps
bw = [50e6/8, 384000/8, 21400/8]
n_model_all = 6
n_remote = 4
k = 10 # scale latency into same range as accuracy
def decision(bandwidth=0, n_face_interval=0,weight=0.5,model_range=[0,n_model_all], cpu_limit = CPU_threshold, gpu_limit = GPU_threshold,energy_limit = 1, speed = None):
    # print bandwidth,latency
    '''
    model, accuracy
    remote: model 0
    '''
    max_utility = float("-inf")
    model_acc = 0
    model = None
    # model_ltc = 0
    for i in range(model_range[0],model_range[1]):
        sigma = bandwidth
        processing = ModelProcessing[i]
        if not speed:
            speed = np.random.randn()*300+float(bw[bandwidth])
        # speed = float(bw[bandwidth])
            speed = float(speed)

        transmission = resolution/speed if i>=n_remote else 0
        total_latency = k * (processing + transmission)
        if i<n_remote: # local model use sigma=0
            accuracy = ModelAccuracy[i][0][n_face_interval]
        else:
            accuracy = ModelAccuracy[i][sigma][n_face_interval]
        
        utility = (1-weight)*accuracy - weight * total_latency
        # utility = accuracy - weight * total_latency
        print('Model %i |UTL: %f| ACC: %f|LTC: %f|PRO: %f|TRM: %f' %(i, utility, accuracy, total_latency, processing,transmission))
        if utility>max_utility:  
            # if using local model: discard model not satisfying constraints
            print("!!!!!!!!!!!!!!!!!", cpu_limit, gpu_limit)
            if i < n_remote and (ModelResource[i][1]>gpu_limit or ModelResource[i][0]>cpu_limit or processing>energy_limit):
                # print("!!!!!!!!!!!cpu gpu limits", ModelResource[i][0], ModelResource[i][1])
                print("trace")
                continue
            model = i 
            max_utility = utility
            model_acc = accuracy
        print("max_utility", max_utility)
    
    transmission = resolution/float(bw[bandwidth])  if i>=n_remote else 0
    print("############",model)
    if model == None:
        model_acc = 0
        latency = 0
    else:
        latency = transmission+ModelProcessing[model]
    return model, model_acc, latency

def fig1(bandwidth, n_face_interval):
    '''
    test our model
    bandwidth is within [0,1,2] (0-4g, 1-3g, 2-2g)
    n_face_interval is within [0,1,2] (0- no limit,1- <10, 2- >=10)
    return selected model (index: 0~5), MAP, latency
    '''
    return decision(bandwidth=bandwidth,n_face_interval=n_face_interval,model_range=[0,n_model_all])

def fig1_local(bandwidth, n_face_interval): 
    '''
    baseline: choose from local models only
    bandwidth is within [0,1,2] (0-4g, 1-3g, 2-2g)
    n_face_interval is within [0,1,2] (0- no limit,1- <10, 2- >=10)
    return selected model (index: 0~5), MAP, latency
    '''
    return decision(bandwidth=bandwidth, n_face_interval=n_face_interval,model_range=[0,n_remote])

def fig1_remote(bandwidth, n_face_interval): 
    '''
    baseline: choose from remote models only
    bandwidth is within [0,1,2] (0-4g, 1-3g, 2-2g)
    return selected model (index: 0~5), MAP, latency
    '''
    return decision(bandwidth,n_face_interval,model_range=[n_remote,n_model_all])

def fig2(cpu, gpu):
    '''
    cpu and gpu are resource limits. Range needs referring data
    return MAP, latency
    '''
    print(cpu,gpu)
    return decision(bandwidth=2,n_face_interval=0,model_range=[0,n_remote],cpu_limit=cpu,gpu_limit=gpu)[1:]

def fig3(weight):
    '''
    weight is for latency, within 0~1 (inclusive)
    return MAP, latency
    '''
    return decision(bandwidth=0,n_face_interval=0,model_range=[0,n_model_all],weight = weight)[1:]

def fig4(face_num):
    '''
    face_num is within [0,1,2] (0- no limit,1- <10, 2- >=10)
    return MAP
    '''
    return decision(bandwidth=0,n_face_interval=face_num,model_range=[0,n_model_all])[1]

# print fig1(0,0)
# print fig1_local(0,0)
# print fig1_remote(0,0)
# print fig2(2000,2000)
# print fig3(0.2)
# print fig4(1)
