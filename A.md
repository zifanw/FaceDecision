## Accuracy Report on Different Model

### DLib Haar Cascade Face Detector
* **Metrics**

    Average IOU = 0.218

    mAP = 0.307

    Average Inferencing time (On CPU) : 0.04s

* **Less than 10 Faces**

    Average IOU = 0.237

    mAP = 0.333

* **More than 10 and Less than 20 Faces**

    Average IOU = 0.124

    mAP = 0.174

* **More than 20 Faces**

    Average IOU = 0.096

    mAP = 0.129

* **Resource Usage (On CPU)**:

    Memory Usage : 414.453 MiB

    CPU Utilization : 680-730%

### DLib HOG Face Detector
* **Metrics**

    Average IOU = 0.253

    mAP = 0.365

    Average Inferencing time (On CPU) : 0.140s

* **Less than 10 Faces**

    Average IOU = 0.296

    mAP = 0.429

* **More than 10 and Less than 20 Faces**

    Average IOU = 0.055

    mAP = 0.0759

* **More than 20 Faces**

    Average IOU = 0.032

    mAP = 0.044

* **Resource Usage (On CPU)**:

    Memory Usage : 270.777 MiB

    CPU Utilization : 99-100%


### DLib CNN MMOD Face Detector
* **Metrics**

    Average IOU = 0.286

    mAP = 0.415

    Average Inferencing time (On GPU) : 0.0452s

    Average Inferencing time (On CPU) : 2.615s

* **Less than 10 Faces**

    Average IOU = 0.340

    mAP = 0.495

* **More than 10 and Less than 20 Faces**

    Average IOU = 0.049

    mAP = 0.07

* **More than 20 Faces**

    Average IOU = 0.02

    mAP = 0.036

* **Resource Usage (On GPU)**:

    Memory Usage : 1171.367 MiB

    GPU Memory Usage : 1037 MiB

    GPU Core Utilization : 75-90%

    CPU Utilization : 99-100%

* **Resource Usage (On CPU)**:

    Memory Usage : 739.69 MiB

    CPU Utilization : 100-123%

### Tensorflow MTCNN Face Detector

* **Metrics**

    Average IOU = 0.417

    mAP = 0.517

    Average Inferencing time (On GPU) : 0.236 s

    Average Inferencing time (On CPU) : 12.078 s

* **Less than 10 Faces**

    Average IOU = 0.430

    mAP = 0.532

* **More than 10 and Less than 20 Faces**

    Average IOU = 0.33

    mAP = 0.42

* **More than 20 Faces**

    Average IOU = 0.38

    mAP = 0.477

* **Resource Usage (On GPU)**:

    Memory Usage : 2074.180 MiB

    GPU Memory Usage : 5004 MiB

    GPU Core Utilization : 10-40%

    CPU Utilization : 111-120%

### Tensorflow MobileNet_SSD Face Detector

#### **Metrics**
* **All Faces**

    Average IOU = 0.598

    mAP = 0.751

    Average Inferencing time (On GPU) : 0.014 s

    Average Inferencing time (On CPU) : 0.578 s

* **Less than 10 Faces**

    Average IOU = 0.621

    mAP = 0.782

* **More than 10 and Less than 20 Faces**

    Average IOU = 0.483

    mAP = 0.608

* **More than 20 Faces**

    Average IOU = 0.479

    mAP = 0.593

* **Resource Usage (On GPU)**:

    Memory Usage : 1967.676 MiB

    GPU Memory Usage : 502 MiB

    GPU Core Utilization : 47-58%

    CPU Utilization : 140-150%

* **Resource Usage (On CPU)**:

    Memory Usage : 390 MiB

    CPU Utilization : 260-290%

### Pytorch SFD Face Detector

* **Metrics**

    Average IOU = 0.647

    mAP = 0.843

    Average inference time (GPU) = 0.088

* **Resource Usage (On GPU)**:

    Memory Usage : 2293.76 MiB

    GPU Memory Usage : 13501 MiB

    GPU Core Utilization : 65%

    CPU Utilization : 220-330%


## Tables

mAP matrix: **6 x 4 x 3**

Resource matrix: **68**, 



c = 0

| Model        | mAP(F)         | mAP(<10) |mAP(10-20)|mAP(>20)|
| ------------- |:-------------:| :----:| :----:|:----:|
| Haar Cascade  | 0.307 | 0.333 | 0.174 | 0.129 |
| HOG+SVM       | 0.365 | 0.429 | 0.423 | 0.044 |
| DLib CNN      | 0.415 | 0.495 | 0.07 | 0.036 |
| MTCNN         | 0.517 | 0.532 | 0.42 | 0.477 |
| MobileNet_SSD | 0.751 | 0.782 | 0.608 | 0.593 |
| SFD           | 0.883 | 0.916 | 0.816 | 0.763 |



c = 1

| Model         | mAP(F) | mAP(<10) | mAP(10-20) | mAP(>20) |
| ------------- | :----: | :------: | :--------: | :------: |
| Haar Cascade  | 0.286  |  0.329   |   0.183    |  0.141   |
| HOG+SVM       | 0.351  |  0.371   |   0.352    |  0.037   |
| DLib CNN      | 0.415  |  0.441   |    0.05    |  0.032   |
| MTCNN         | 0.499  |  0.531   |   0.382    |  0.410   |
| MobileNet_SSD | 0.671  |  0.722   |   0.514    |  0.508   |
| SFD           | 0.879  |  0.910   |   0.814    |  0.745   |



c = 3

| Model         | mAP(F) | mAP(<10) | mAP(10-20) | mAP(>20) |
| ------------- | :----: | :------: | :--------: | :------: |
| Haar Cascade  | 0.274  |  0.316   |   0.131    |  0.076   |
| HOG+SVM       | 0.334  |  0.359   |   0.318    |  0.013   |
| DLib CNN      | 0.365  |  0.443   |   0.044    |  0.023   |
| MTCNN         | 0.441  |  0.473   |   0.364    |  0.163   |
| MobileNet_SSD | 0.311  |   0.36   |   0.122    |  0.098   |
| SFD           | 0.801  |  0.832   |   0.812    |  0.742   |



| Model         | Latency (CPU) | Latency (GPU) |
| ------------- | :-----------: | :-----------: |
| Haar Cascade  |     0.040     |      N/A      |
| HOG+SVM       |     0.140     |      N/A      |
| DLib CNN      |     2.615     |     0.045     |
| MTCNN         |    12.078     |     0.236     |
| MobileNet_SSD |     0.578     |     0.014     |
| SFD           |     5.168     |     0.088     |



| Model         | CPU Memory Usage  (on CPU) | CPU Memory Usage (on GPU) | GPU Memory Usage |
| :------------ | :------------------------: | :-----------------------: | :--------------: |
| Haar Cascade  |        414.453 MiB         |            N/A            |       N/A        |
| HOG+SVM       |      **270.777 MiB**       |            N/A            |       N/A        |
| DLib CNN      |        876.234 MiB         |     **1171.367 MiB**      |     1037 MiB     |
| MTCNN         |          6984 MiB          |       2074.180 MiB        |     5004 MiB     |
| MobileNet_SSD |          390 MiB           |       1967.676 MiB        |   **502 MiB**    |
| SFD           |            N/A             |        2293.76 MiB        |    13501 MiB     |
