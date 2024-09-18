<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Calibri', Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
            overflow: hidden; 
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 800px; 
            width: 100%; 
        }
        input {
            padding: 10px;
            font-size: 16px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            width: 100%; 
            box-sizing: border-box;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%; 
            box-sizing: border-box;
        }
        button:hover {
            background-color: #0056b3;
        }
        p {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin: 20px 0 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Binary Calculator</h1>
        <input type="number" id="numberInput" placeholder="Enter an integer" />
        <button onclick="convertToBinary()">Convert to Binary</button>
        <p id="result"></p>
    </div>
    <script>
        function convertToBinary() {
            const numberInput = document.getElementById('numberInput').value;
            const resultElement = document.getElementById('result');
            if (numberInput.trim() === '') {
                resultElement.textContent = 'Please enter a number or integer.';
                return;
            }  
            const number = parseInt(numberInput, 10);
            if (isNaN(number) || number < 0) {
                resultElement.textContent = 'Please enter a non-negative integer.';
                return;
            }
            const binary = number.toString(2);
            resultElement.textContent = `The binary representation of ${number} is: ${binary}`;
        }
    </script>
</body>
</html>