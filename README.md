# Welcome to BuellerBot V1 👋

🤖 Meet BuellerBot: Your AI-powered clone that joins online meetings, listens for your name, and then responds with *your* voice - all so you don’t have to. 

## Realtime Demo of BuellerBot in Action!

https://github.com/EdwardIPAguilar/BuellerBot/assets/59296703/7bc4bfa1-8104-4ffb-964f-87159ac144a5

## Table of Contents

1. [Installation](#installation)
2. [Contributing](#contributing)
3. [Questions](#questions)

## ⚙️ Installation

### Prerequisites
Python >=3.8.0
An OpenAI API key that can access OpenAI API (set up a paid account OpenAI account)
An ElevenLabs API key that can access the EL API (set up a paid account EL account)
macOS or Windows (audio routing setup required)

### Setting Up Audio Routing
BuellerBot captures system audio through a virtual audio device so it can listen in without creating feedback.

#### macOS: Blackhole
You can get Blackhole for free at https://existential.audio/blackhole/

  - Once you've downloaded Blackhole (make sure it's the 2ch version), you'll need to setup a MIDI multi-output device. This is super easy on macOS.
  - Open the **Audio MIDI setup** app, click the plus button at the bottom right, select **Multi-output-device**, and choose Blackhole along with any other devices you want your audio output to route to. Viola, audio device created!
  - To make sure audio is routed through Blackhole as well as your other output devices, right click the newly created output device on the left-side menu and select **use this device for sound output**.
  - Sometimes you might not see anything showing up when transcribing; the most likely cause is that you haven't selected **use this device for sound output**. This resets every now and again if you're frequently connecting and disconnecting the output devices it relies on.

#### Windows: VB-Audio Virtual Cable
Install the free VB-Audio Virtual Cable from https://vb-audio.com/Cable/

  - After installation, open the Windows **Sound** settings and set **CABLE Output** as the default playback device.
  - If you name the device differently, set `AUDIO_DEVICE_NAME` in your `.env` file to match so `recorder.py` can find it.

P.S. Input is typically handled within the platform you're using.

### Connecting BuellerBot To Your ElevenLabs + OpenAI Account
Create a `.env` file and set `EL_API_KEY` and `OPEN_AI_KEY` to your API keys.
Optionally set `AUDIO_DEVICE_NAME` to override the audio device that `recorder.py`
should use (e.g., `AUDIO_DEVICE_NAME="CABLE Output"` on Windows if you rename the VB-Audio device).

### Enabling SMS Check-In (Optional)
If you'd like BuellerBot to text you a code whenever the teacher says "check in," add your Twilio credentials to `.env`:

```
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_FROM_PHONE=+15551234567      # Twilio phone number
TWILIO_TO_PHONE=+15557654321        # Your phone number
```

When "check in" is detected in the live transcript, BuellerBot will generate a random 6‑digit code and send it to `TWILIO_TO_PHONE` via SMS.

### Running on GitHub Actions
A minimal workflow is provided in `.github/workflows/python.yml` that installs dependencies and runs a syntax check on the source files. To use it, add your `EL_API_KEY` and `OPEN_AI_KEY` as repository secrets so the code can authenticate with OpenAI and ElevenLabs when needed.

## Contributing

This project is open for suggestions and contributions! In case it's your first time (as is mine), here's how you can do so:

Fork the repository: Click on the 'Fork' button at the top right corner of this page. This will create a copy of this repository in your account.

Clone the repository to your local machine: Click on the 'Code' button (usually green and located at the right of the repo's name), copy the URL, then open a terminal on your machine, navigate to the directory you want, and run

```
git clone URL
Replace URL with the url you just copied.
```

Create a branch where you can make your changes. From the terminal inside your project directory, run

```
git checkout -b branch-name
Replace branch-name with a name related to the feature you want to work on or the bug you want to fix.
```

Make your changes in this new branch.
Then, commit and push your changes. From your terminal, run

```
git add .
git commit -m "Your commit message"
git push origin branch-name
```

Replace branch-name with the name of the branch you created earlier and "Your commit message" with a description of the changes you've made.

Once you've pushed your changes to GitHub, you can create a pull request. Go to the repository page in your account, and you will see a 'Compare & pull request' button. Click on it, add further details if needed, and then click on 'Create pull request'.

If you have any suggestions, questions, or bugs to report, please open an issue in this repository! I will do my best to work on them :)

## ✍️ Questions

If you have any questions or ideas, feel free to reach out at aguilare@lakeforest.edu!

## ⚠️ Disclaimer
Buellerbot was built for *educational* purposes only. As in, you should use any free-time gained with BB to educate yourself in what matters. 

*"Life moves pretty fast. If you don't stop and look around once in a while, you could miss it."* - Ferris Bueller's Day Off, 1986

## 🏆 Acknowledgements

S/O to Michael, thank you Michael
