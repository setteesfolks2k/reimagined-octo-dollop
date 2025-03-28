function calculateBMI(weight, height) {
    let bmi = weight / (height * height);
    console.log(`⚖️ Your BMI is: ${bmi.toFixed(2)}`);
    if (bmi < 18.5) console.log("📉 Underweight");
    else if (bmi < 24.9) console.log("✅ Normal weight");
    else if (bmi < 29.9) console.log("⚠️ Overweight");
    else console.log("🚨 Obese");
}

calculateBMI(70, 1.75); // Example: 70kg, 1.75m
