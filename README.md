🎨 AuraColor AI: Seasonal Color Analysis
AuraColor AI is a computer vision-powered web application designed to help users discover their seasonal color palette (Spring, Summer, Autumn, or Winter). By leveraging K-Means Clustering, the app mathematically extracts skin undertones and luminance to provide personalized fashion and style recommendations.
🧠 The Data Science Behind ItThis project moves beyond simple color picking by implementing a robust data pipeline:Region of Interest (ROI) Selection: The system automatically focuses on the central facial region to minimize noise from backgrounds or clothing.K-Means Clustering: Using the scikit-learn library, the model partitions pixel data into clusters to find the most dominant skin tone centroid, effectively handling shadows and highlights.Two-Factor Classification:Hue Analysis ($R$ vs $B$): Determines if the undertone is "Warm" or "Cool."Luminance Analysis: Calculates the perceived brightness using the formula: $Y = 0.299R + 0.587G + 0.114B$.Seasonal Mapping: The intersection of Hue and Luminance maps the user into one of the four seasonal categories:Spring: Warm + LightAutumn: Warm + DarkSummer: Cool + LightWinter: Cool + Dark🛠️ Tech StackLanguage: PythonUI Framework: StreamlitComputer Vision: OpenCVMachine Learning: Scikit-Learn (K-Means Clustering)Deployment: Streamlit Community Cloud

🧪 Methodology & Technical Implementation
The AuraColor AI engine follows a structured Data Science pipeline to ensure accuracy and mathematical consistency.

1. Image Pre-processing & ROI Selection
To reduce computational noise, the application identifies a Region of Interest (ROI). By focusing on the central coordinates of the uploaded image, we isolate facial skin pixels and exclude background interference, hair, and clothing.

2. Unsupervised Learning: K-Means Clustering
Instead of simple color averaging, which is sensitive to shadows, we implement K-Means Clustering.
The Goal: To partition $n$ pixels into $k$ clusters ($k=3$).The Math: The algorithm minimizes the within-cluster sum of squares (WCSS), finding the mathematical "centroid" of the skin tone.
<img width="358" height="113" alt="image" src="https://github.com/user-attachments/assets/b187bb2a-9c3f-4a13-a347-e6b838c108cd" />
3. Feature Engineering: Luminance & HueWe transform raw RGB data into two primary features for classification:Hue Detection: We compare the Red ($R$) and Blue ($B$) channels. If R > B, the undertone is classified as Warm; otherwise, it is Cool.Luminance Calculation ($Y$): To determine if a skin tone is "Light" or "Deep," we use the standard digital CCIR 601 weights:
   <img width="543" height="83" alt="image" src="https://github.com/user-attachments/assets/a4750ef9-5813-4a56-a15d-9d66cc800a54" />
4. The Decision Matrix
The final prediction is made using a 4-quadrant classification logic:
Feature Set,Condition,Predicted Season
Warm + Light,R>B and Y>140,Spring 🌸
Warm + Dark,R>B and Y≤140,Autumn 🍂
Cool + Light,R<B and Y>140,Summer 🏖️
Cool + Dark,R<B and Y≤140,Winter ❄️
Aura Color is very useful 
