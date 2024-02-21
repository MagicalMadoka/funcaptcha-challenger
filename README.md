# funcaptcha challenger

## Introduction

Just `ai vs ai`

## Features

| Challenge Type                | Prompt                                                                                 | Demo                                                                             |
|-------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| 3d_rollball_animals           | Use the arrows to rotate the animal to face in the direction of the hand               | [3d_rollball_animals_demo](demo/3d_rollball_animals_demo.py)                     |
| 3d_rollball_objects           | Use the arrows to rotate the object to face in the direction of the hand               | [3d_rollball_objects_demo](demo/3d_rollball_objects_demo.py)                     |
| numericalmatch                | Use the arrows to change the number of objects until it matches the left image         | 🚧                                                                               |
| hopscotch_highsec             | Use the arrows to move the person to the icon indicated by the colored circle          | [hopscotch_highsec_demo](demo/hopscotch_highsec_demo.py)                         |
| icon_connect                  | Using the arrows, connect the same two icons with the dotted line as shown on the left | 🚧                                                                               |
| coordinatesmatch              | Using the arrows, move the person to the indicated seat                                | [coordinatesmatch_demo](demo/coordinatesmatch_demo.py)                           |
| train_coordinates             | Use the arrows to move the train to the coordinates indicated in the left image        | [train_coordinates_demo](demo/train_coordinates_demo.py)                         |
| BrokenJigsawbrokenjigsaw_swap |                                                                                        | [BrokenJigsawbrokenjigsaw_swap_demo](demo/BrokenJigsawbrokenjigsaw_swap_demo.py) |
| shadows                       | Pick the wrong shadow                                                                  | [shadows_demo](demo/shadows_demo.py)                                             |
| penguins                      | Pick the penguin                                                                       | [penguin_demo](demo/penguins_demo.py)                                            |
| frankenhead                   | Select the animal with the wrong head                                                  | [frankenhead_demo](demo/frankenhead_demo.py)                                     |
| counting                      | Pick the image where the number matches the amount of animals                          | [counting_demo](demo/counting_demo.py)                                           |
| ...                           | ...                                                                                    | 🚧                                                                               |

## Installation

```bash
pip install funcaptcha-challenger
```

##  Server Usage Example

- **Install**:
```bash
pip install server/requirements.txt
```
- **Run**:
```bash
python server/main.py
```

- **Curl Request**:

    Replace the image below with a base64 encoded picture.

```bash
curl --location --request POST 'http://127.0.0.1:8181/createTask' \
--header 'Content-Type: application/json' \
--data-raw '
    {
        "image": Input Image base64 encoding,
        "variant": "3d_rollball_objects"
    }
}'
```

- **Response Example**:

```json
 {
  "errorCode": "",
  "errorId": 0,
  "solution": {
    "objects": [
      4
    ]
  },
  "status": "ready",
  "taskId": "bb11d056130b5e41f3d870edfa21c6a4"
}
```

- **Recognition instructions**:

> errorId: 0 Recognition successful.\
> objects: Corresponding recognition result\
> Counting from 0.`"objects": [4]` \
> Indicates that the recognition result is sequence 4.

## Sponsors

### [Capsolver](https://capsolver.com?utm_source=github&utm_medium=banner_github&utm_campaign=funcaptcha_challenger)

[![Capsolver](doc/sponsors.gif)](https://capsolver.com?utm_source=github&utm_medium=banner_github&utm_campaign=funcaptcha_challenger)

[Capsolver.com](https://capsolver.com?utm_source=github&utm_medium=banner_github&utm_campaign=funcaptcha_challenger) is
an AI-powered service that provides automatic captcha solving capabilities. It supports a range of captcha types,
including reCAPTCHA, hCaptcha, FunCaptcha, AWS Captcha, Geetest and image captcha. It aims to
facilitate seamless web automation by bypassing captcha verifications efficiently.

## Discussion

- 📱 [Telegram](https://t.me/+iNf8qQk0KUpkYmEx)
