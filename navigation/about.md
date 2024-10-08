---
layout: page
permalink: /about/
title: About Me
---

![Me](download.png)
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .flag {
            width: 300px; 
            height: auto; 
            display: block; 
            margin: 10px auto; 
            border: 5px solid #000;  
        }
        h1 {
            color: #FA8072;
        }
        .me {
            width: 300px; 
            height: auto; 
            display: block; 
            margin: 0 auto; 
            border: 5px solid #000; 
        }
    </style>
</head>
<body>
    <div class="container"> 
        <h1>Family and Nationality</h1>
        <div id="family">
            <p>I live with two parents and an older sibling, who graduated from Del Norte and now attends community college. Both of my parents are Vietnamese immigrants, who moved into the U.S around the early 1990s. The vast majority of my immediate family lives in Seattle, Washington, whom we visit at least once a year.</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Flag_of_South_Vietnam.png/1024px-Flag_of_South_Vietnam.png" alt="Vietnamese Flag" class="flag">
        </div>
        <h1>Future Plans 🚀</h1>
        <div id="passions">
            <p>I plan on pursuing a career in electrical engineering. I do intend to pursue a master's at some point. I may attend community college initially but then transfer to a UC school (UCSD). However, I am currently undecided in that regard.</p>
        </div>
        <h1>Things I Do In My Free Time 🎵🎮📚</h1>
        <div id="things">
            <p>One of my favorite things to do is listen to music. My current favorite genre is "dreampop," but I do listen to other genres such as synthwave, indie, and even rock. I also enjoy playing video games, but since school started, I haven't had as much time. I love reading as well. I read primarily fiction, but I do pick up an occasional nonfiction book.</p>
        </div>
        <h1>Interesting Facts 🤔🚴‍♂️🥋</h1>
        <div id="interesting">
            <p>One of the "weirder" things about me is that I'm double-jointed on both thumbs. To my knowledge, I'm not double-jointed anywhere else. I love biking, and I actually participated in a 250-mile bike ride in fifth grade (RAC or Ride Across California). I've played around 3 sports in total. I played soccer for a year at best, swam for 2 years at best, and did karate (self-defense) for around 5 years. I made it to brown belt but then quit once I had reached high school.</p>
        </div>
    </div>
    <script src="https://utteranc.es/client.js"
        repo="Ryan378-code/ryan1_2025"
        issue-term="pathname"
        theme="github-dark"
        crossorigin="anonymous"
        async>
    </script>
    <script>
        var family = document.getElementById('family');
        var passions = document.getElementById('passions');
        var things = document.getElementById('things');
        var interesting = document.getElementById('interesting');
        family.style.marginBottom = '20px';
        passions.style.marginBottom = '20px';
        things.style.marginBottom = '20px';
        interesting.style.marginBottom = '20px';
    </script>
</body>
</html>
