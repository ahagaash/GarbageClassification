import werkzeug
import cv2
from flask import Flask ,request,jsonify
import sendmail
app = Flask(__name__)
import mongo


@app.route('/upload',methods=["POST"])
def upload():
    if(request.method =="POST"):
        message="processing started"
        imagefile=request.files["image"]
        filename=werkzeug.utils.secure_filename(imagefile.filename)
        print(filename)
        imagefile.save("./uploadedImages/"+filename)
        message="image file uploaded in our system but some error in our server "
        net = cv2.dnn.readNet("./dnn/yolov4-custom_best.weights",
                              "./dnn/yolov4-custom.cfg")
        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(size=(416, 416), scale=1 / 255)

        # Load class list
        classes = []
        with open("./dnn/obj.names") as file_object:
            for class_name in file_object.readlines():
                class_name = class_name.strip()
                classes.append(class_name)

        #
        frame = cv2.imread("./uploadedImages/"+filename)
        # object Detection
        (class_ids, scores, bboxes) = model.detect(frame)
        sum = 0
        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            (x, y, w, h) = bbox
            class_name = classes[class_id]

            if class_name == "glass" or class_name == "metal" or class_name == "plastic":
                waste=class_name
                try:
                  if(sum==0):
                      mongo.getDatafromDataBASEALL(waste, "wa", "Detected")

                      sendmail.sendEmailToUser(waste, "ahagaash@gmail.com", "Detected")
                      sum = sum + 1



                except:
                   break
                   message = "Internal server Error 500 waste collectors details not found"
                else:
                    message = "Waste detected as " +waste+" waste clollectors details send to your email"

                try:
                    mongo.getDatafromDataBASE(waste, "wa", "Detected_Based_On-Adress")
                    sendmail.sendEmailToUserbasedonAddress(waste, "ahagaash@gmail.com", "Detected_Based_On-Adress")
                    message = "waste have detected as " + class_name + " details of collectors near your zipcode  will be mailed to you"
                    cv2.destroyAllWindows()
                    break

                except :
                    message = message+ " sorry waste collectors based on zip code not found"

                else :
                    message = message+" waste have detected as " + class_name + " details of collectors near your zipcode  will be mailed to you"





            if class_name == "paper" or class_name == "cardboard" or class_name == "trash":
                print("cannot able to recycled")
                message="cannot able to find any recyclable waste please upload any other image to find collectors"
                cv2.destroyAllWindows()
                break





    return jsonify({
        "message": message
    })






@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! it is workingddddddddd'




if __name__ == '__app__':
    app.run(debug=True , port=4000)
