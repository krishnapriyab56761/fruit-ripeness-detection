const input = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const button = document.getElementById("predictBtn");
const loading = document.getElementById("loading");
const fruit = document.getElementById("fruit");
const confidence = document.getElementById("confidence");
const speakBtn = document.getElementById("speakBtn");

let predictedClass = null;
// ----------------------------------------
// Speak only when user clicks the button
// ----------------------------------------

speakBtn.addEventListener("click", function () {

    if (!predictedClass) {

        alert("Please predict a fruit first.");

        return;
    }

    speakPrediction(predictedClass);

});

// ----------------------------------------
// Fruit translations
// ----------------------------------------

const fruitTranslations = {

    FreshApple: {
        en: "Fresh Apple",
        ml: "പുതിയ ആപ്പിൾ",
        kn: "ತಾಜಾ ಸೇಬು",
        hi: "ताज़ा सेब",
        ta: "புதிய ஆப்பிள்"
    },

    RottenApple: {
        en: "Rotten Apple",
        ml: "ചീഞ്ഞ ആപ്പിൾ",
        kn: "ಕೊಳೆತ ಸೇಬು",
        hi: "सड़ा हुआ सेब",
        ta: "அழுகிய ஆப்பிள்"
    },

    FreshBanana: {
        en: "Fresh Banana",
        ml: "പുതിയ വാഴപ്പഴം",
        kn: "ತಾಜಾ ಬಾಳೆಹಣ್ಣು",
        hi: "ताज़ा केला",
        ta: "புதிய வாழைப்பழம்"
    },

    RottenBanana: {
        en: "Rotten Banana",
        ml: "ചീഞ്ഞ വാഴപ്പഴം",
        kn: "ಕೊಳೆತ ಬಾಳೆಹಣ್ಣು",
        hi: "सड़ा हुआ केला",
        ta: "அழுகிய வாழைப்பழம்"
    },

    FreshGrape: {
        en: "Fresh Grape",
        ml: "പുതിയ മുന്തിരി",
        kn: "ತಾಜಾ ದ್ರಾಕ್ಷಿ",
        hi: "ताज़ा अंगूर",
        ta: "புதிய திராட்சை"
    },

    RottenGrape: {
        en: "Rotten Grape",
        ml: "ചീഞ്ഞ മുന്തിരി",
        kn: "ಕೊಳೆತ ದ್ರಾಕ್ಷಿ",
        hi: "सड़ा हुआ अंगूर",
        ta: "அழுகிய திராட்சை"
    },

    FreshGuava: {
        en: "Fresh Guava",
        ml: "പുതിയ പേരയ്ക്ക",
        kn: "ತಾಜಾ ಸೀಬೆಹಣ್ಣು",
        hi: "ताज़ा अमरूद",
        ta: "புதிய கொய்யாப்பழம்"
    },

    RottenGuava: {
        en: "Rotten Guava",
        ml: "ചീഞ്ഞ പേരയ്ക്ക",
        kn: "ಕೊಳೆತ ಸೀಬೆಹಣ್ಣು",
        hi: "सड़ा हुआ अमरूद",
        ta: "அழுகிய கொய்யாப்பழம்"
    },

    FreshJujube: {
        en: "Fresh Jujube",
        ml: "പുതിയ ഇലന്തപ്പഴം",
        kn: "ತಾಜಾ ಬೋರೆಹಣ್ಣು",
        hi: "ताज़ा बेर",
        ta: "புதிய இலந்தைப்பழம்"
    },

    RottenJujube: {
        en: "Rotten Jujube",
        ml: "ചീഞ്ഞ ഇലന്തപ്പഴം",
        kn: "ಕೊಳೆತ ಬೋರೆಹಣ್ಣು",
        hi: "सड़ा हुआ बेर",
        ta: "அழுகிய இலந்தைப்பழம்"
    },

    FreshOrange: {
        en: "Fresh Orange",
        ml: "പുതിയ ഓറഞ്ച്",
        kn: "ತಾಜಾ ಕಿತ್ತಳೆ",
        hi: "ताज़ा संतरा",
        ta: "புதிய ஆரஞ்சு"
    },

    RottenOrange: {
        en: "Rotten Orange",
        ml: "ചീഞ്ഞ ഓറഞ്ച്",
        kn: "ಕೊಳೆತ ಕಿತ್ತಳೆ",
        hi: "सड़ा हुआ संतरा",
        ta: "அழுகிய ஆரஞ்சு"
    },

    FreshPomegranate: {
        en: "Fresh Pomegranate",
        ml: "പുതിയ മാതളനാരങ്ങ",
        kn: "ತಾಜಾ ದಾಳಿಂಬೆ",
        hi: "ताज़ा अनार",
        ta: "புதிய மாதுளை"
    },

    RottenPomegranate: {
        en: "Rotten Pomegranate",
        ml: "ചീഞ്ഞ മാതളനാരങ്ങ",
        kn: "ಕೊಳೆತ ದಾಳಿಂಬೆ",
        hi: "सड़ा हुआ अनार",
        ta: "அழுகிய மாதுளை"
    },

    FreshStrawberry: {
        en: "Fresh Strawberry",
        ml: "പുതിയ സ്ട്രോബെറി",
        kn: "ತಾಜಾ ಸ್ಟ್ರಾಬೆರಿ",
        hi: "ताज़ा स्ट्रॉबेरी",
        ta: "புதிய ஸ்ட்ராபெர்ரி"
    },

    RottenStrawberry: {
        en: "Rotten Strawberry",
        ml: "ചീഞ്ഞ സ്ട്രോബെറി",
        kn: "ಕೊಳೆತ ಸ್ಟ್ರಾಬೆರಿ",
        hi: "सड़ी हुई स्ट्रॉबेरी",
        ta: "அழுகிய ஸ்ட்ராபெர்ரி"
    }
};


// ----------------------------------------
// Image Preview
// ----------------------------------------

input.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) {
        return;
    }

    preview.src = URL.createObjectURL(file);

    preview.style.display = "block";

});


// ----------------------------------------
// English Voice Output
// ----------------------------------------

function speakPrediction(className) {

    const translation = fruitTranslations[className];

    if (!translation) {
        return;
    }

    // Speak English only
    const text = translation.en;

    // Stop previous speech
    window.speechSynthesis.cancel();

    const speech =
        new SpeechSynthesisUtterance(text);

    speech.lang = "en-US";
    speech.rate = 0.9;
    speech.pitch = 1.0;
    speech.volume = 1.0;

    window.speechSynthesis.speak(speech);

}


// ----------------------------------------
// Predict Button
// ----------------------------------------

button.addEventListener("click", async function () {

    console.log("Predict button clicked");


    // Check image
    if (!input.files || input.files.length === 0) {

        alert("Please select an image first.");

        return;
    }


    loading.style.display = "block";

    button.disabled = true;


    const formData = new FormData();

    formData.append(
        "image",
        input.files[0]
    );


    try {

        console.log("Sending image to Flask...");


        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",
                body: formData
            }
        );


        console.log(
            "Server response:",
            response.status
        );


        const data = await response.json();


        console.log(
            "Prediction:",
            data
        );


        if (!response.ok) {

            throw new Error(
                data.error || "Prediction failed"
            );

        }
         predictedClass = data.class;

        // --------------------------------
        // Display multilingual fruit name
        // --------------------------------


        
        const translation = fruitTranslations[data.class];

        if (translation) {

            fruit.innerHTML =
                "<b>English:</b> " + translation.en +
                "<br><b>മലയാളം:</b> " + translation.ml +
                 "<br><b>ಕನ್ನಡ:</b> " + translation.kn +
                "<br><b>हिन्दी:</b> " + translation.hi +
                "<br><b>தமிழ்:</b> " + translation.ta;

        } else {

            fruit.innerHTML ="<b>Fruit:</b> " + data.class;
    }

        // --------------------------------
        // Confidence
        // --------------------------------

        confidence.innerHTML =

            "<b>Confidence:</b> " +
            data.confidence +
            " %";


        


    }
    catch (error) {

        console.error(
            "Prediction error:",
            error
        );

        alert(
            "Could not connect to the prediction server."
        );

    }
    finally {

        loading.style.display = "none";

        button.disabled = false;

    }

});