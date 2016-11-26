
sampleDescriptor = {
    "faces": [{"gender": "Male", "age": 34, "faceRectangle": {"width": 215, "top": 463, "height": 215, "left": 157}},
              {"gender": "Male", "age": 35, "faceRectangle": {"width": 92, "top": 676, "height": 92, "left": 478}},
              {"gender": "Male", "age": 30, "faceRectangle": {"width": 87, "top": 569, "height": 87, "left": 992}},
              {"gender": "Male", "age": 27, "faceRectangle": {"width": 69, "top": 555, "height": 69, "left": 512}},
              {"gender": "Female", "age": 25, "faceRectangle": {"width": 60, "top": 513, "height": 60, "left": 924}},
              {"gender": "Male", "age": 30, "faceRectangle": {"width": 51, "top": 460, "height": 51, "left": 644}},
              {"gender": "Female", "age": 33, "faceRectangle": {"width": 49, "top": 470, "height": 49, "left": 880}},
              {"gender": "Male", "age": 34, "faceRectangle": {"width": 42, "top": 433, "height": 42, "left": 740}}],
    "metadata": {"width": 1334, "format": "Jpeg", "height": 1001},
    "description": {
        "captions": [{"text": "Evanna Lynch et al. sitting at a table eating food", "confidence": 0.9383536254186131}],
        "tags": ["person", "table", "group", "sitting", "building", "people", "indoor", "food", "eating", "meal",
                 "posing", "restaurant", "large", "dinner", "man", "long", "glasses", "plate", "wine", "pizza",
                 "room"]}, "requestId": "9a667aaa-7234-44cd-89c4-e0657668334c"}

emotions = json.loads("""{"emotions": [
           {
               "faceRectangle": {
                   "width": 215,
                   "top": 463,
                   "left": 157,
                   "height": 215
               },
               "scores": {
                   "sadness": 0.000379602425,
                   "neutral": 0.138443574,
                   "contempt": 0.008439364,
                   "disgust": 0.0003618463,
                   "anger": 3.47116256e-05,
                   "surprise": 2.60757752e-05,
                   "fear": 5.644057e-07,
                   "happiness": 0.852314234
               }
           },
           {
               "faceRectangle": {
                   "width": 92,
                   "top": 676,
                   "left": 478,
                   "height": 92
               },
               "scores": {
                   "sadness": 0.00059917,
                   "neutral": 0.694292545,
                   "contempt": 0.012415654,
                   "disgust": 0.0006680707,
                   "anger": 0.00267467415,
                   "surprise": 0.00361085683,
                   "fear": 9.70010442e-05,
                   "happiness": 0.285642028
               }
           },
           {
               "faceRectangle": {
                   "width": 87,
                   "top": 569,
                   "left": 992,
                   "height": 87
               },
               "scores": {
                   "sadness": 0.0216562673,
                   "neutral": 0.0462055877,
                   "contempt": 0.0687164441,
                   "disgust": 0.0978033245,
                   "anger": 0.007973234,
                   "surprise": 0.0009310261,
                   "fear": 0.0001383493,
                   "happiness": 0.756575763
               }
           },
           {
               "faceRectangle": {
                   "width": 69,
                   "top": 555,
                   "left": 512,
                   "height": 69
               },
               "scores": {
                   "sadness": 0.000628587848,
                   "neutral": 0.9855761,
                   "contempt": 0.00272841,
                   "disgust": 2.02703868e-05,
                   "anger": 8.797132e-05,
                   "surprise": 0.000130697663,
                   "fear": 8.053151e-06,
                   "happiness": 0.010819925
               }
           },
           {
               "faceRectangle": {
                   "width": 60,
                   "top": 513,
                   "left": 924,
                   "height": 60
               },
               "scores": {
                   "sadness": 0.000241876638,
                   "neutral": 0.00415524375,
                   "contempt": 0.000387048931,
                   "disgust": 4.528864e-06,
                   "anger": 2.397539e-06,
                   "surprise": 2.79194069e-06,
                   "fear": 2.32335665e-07,
                   "happiness": 0.9952059
               }
           },
           {
               "faceRectangle": {
                   "width": 51,
                   "top": 460,
                   "left": 644,
                   "height": 51
               },
               "scores": {
                   "sadness": 0.00369153661,
                   "neutral": 0.897447765,
                   "contempt": 0.00754997041,
                   "disgust": 0.000520122354,
                   "anger": 0.0004030356,
                   "surprise": 0.000434813148,
                   "fear": 4.36986229e-05,
                   "happiness": 0.08990904
               }
           },
           {
               "faceRectangle": {
                   "width": 49,
                   "top": 470,
                   "left": 880,
                   "height": 49
               },
               "scores": {
                   "sadness": 5.883904e-07,
                   "neutral": 2.88642132e-05,
                   "contempt": 1.43325352e-07,
                   "disgust": 5.08088169e-06,
                   "anger": 1.7595936e-06,
                   "surprise": 2.49779646e-07,
                   "fear": 6.925049e-09,
                   "happiness": 0.9999633
               }
           },
           {
               "faceRectangle": {
                   "width": 42,
                   "top": 433,
                   "left": 740,
                   "height": 42
               },
               "scores": {
                   "sadness": 0.0131007275,
                   "neutral": 0.7388378,
                   "contempt": 0.0132363709,
                   "disgust": 0.000342020736,
                   "anger": 7.826331e-05,
                   "surprise": 0.000728650542,
                   "fear": 3.29896829e-05,
                   "happiness": 0.233643189
               }
           }
       ]}""")
