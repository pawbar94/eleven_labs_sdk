![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/pawbar94/eleven_labs_sdk/linux-tests.yml?label=Linux%20tests) ![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/pawbar94/eleven_labs_sdk/windows-tests.yml?label=Windows%20tests) [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# ElevenLabs SDK for Python
Table of contents:

[What is it?](#what_is_it)<br>
[How to use](#how_to_use)<br>
[ElevenLabs API client](#eleven_labs_api_client)<br>
&emsp;[Creating api object](#creating_api_object)<br>
&emsp;[Getting available voices](#getting_available_voices)<br>
&emsp;[Converting text to audio](#converting_text_to_audio)<br>
&emsp;[Converting text to audio stream](#converting_text_to_audio_stream)<br>
&emsp;[Getting default voice settings](#getting_default_voice_settings)<br>
&emsp;[Getting voice settings](#getting_voice_settings)<br>
&emsp;[Getting specific voice](#getting_specific_voice)<br>
&emsp;[Deleting specific voice](#deleting_specific_voice)<br>
&emsp;[Editing voice settings](#editing_voice_settings)<br>
&emsp;[Adding new voice](#adding_new_voice)<br>
&emsp;[Editing voice](#editing_voice)<br>
&emsp;[Deleting voice sample](#deleting_voice_sample)<br>
&emsp;[Getting audio from sample](#getting_audio_from_sample)<br>
&emsp;[Getting generated items](#getting_generated_items)<br>
&emsp;[Getting audio from history item](#getting_audio_from_history_item)<br>
&emsp;[Deleting history item](#deleting_history_item)<br>
&emsp;[Downloading history items](#downloading_history_items)<br>
&emsp;[Getting user subscription info](#getting_user_subscription_info)<br>
&emsp;[Getting user info](#getting_user_info)<br>

## <a name="what_is_it"></a>What is it?

ElevenLabs SDK for Python is a Python module which is supposed to deliver a bunch of programming tools which make usage of ElevenLabs text-to-speech conversion service easier and help developing full solutions. Currently available tools are:
* ElevenLabs API client

But there is a plan for further development.

## <a name="how_to_use"></a>How to use

This repository is a Python module, so in order to use it, just add it as a submodule to your project (or clone it somewhere within your project) and import the required stuff (more detailed description below).

# ElevenLabs API client

The full documentation of the API created by ElevenLabs may be found here: https://api.elevenlabs.io/docs .

## <a name="creating_api_object"></a>Creating api object

In order to create an api object, just import the `ElevenLabsApi` class from `eleven_labs_sdk` module and create an instance of it. You must pass your api key as a parameter to the constructor.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
```

## <a name="getting_available_voices"></a>Getting available voices

In order to get all available voices on your account, just call the `get_voices` method of the `ElevenLabsApi` object. This method returns a list of `Voice` objects representing properties of each voice.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Print voices' properties
print('All voices:')
for voice in all_voices:
    print(f' * {voice}')
```

For the default voices, you will see output like this (properties of each voice shown below are much longer, but here they are shortened for readability):

```
[INFO][ElevenLabsApi] Getting available voices
All voices:
 * Voice(id='21m00Tcm4TlvDq8ikWAM', name='Rachel', samples=[], category='premade', ...)
 * Voice(id='AZnzlk1XvdvUeBnXmlld', name='Domi', samples=[], category='premade', ...)
 * Voice(id='EXAVITQu4vr4xnSDxMaL', name='Bella', samples=[], category='premade', ...)
 ...
```

## <a name="converting_text_to_audio"></a>Converting text to audio

In order to convert text to speech and save it to audio file, first of all choose voice that you want to use for the speech generation. There are couple of ways to do it, one of the is to filter out the desired voice by name from the list of all available voices:

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Chose the desired voice and extract it from the list
sam_voice: Voice = list(filter(lambda x: x.name == 'Sam', all_voices))[0]
```

Then, the simplest way to convert text to speech using the chosen voice is to call the `text_to_speech` method providing only the voice's ID and the text to convert:

```python
# Text to convert
text: str = 'Hello world!'
# Send text to speech conversion request
audio_data: bytes = api.text_to_speech(sam_voice.id, text)
# Save audio to file
with open('audio.mp3', 'wb') as file:
    file.write(audio_data)
```

However, there are additional optional parameters which you can specify to have a greater control over the conversion.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, Voice, ModelId, LatencyOptimization
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Get all voices available on your account
all_voices: List[Voice] = api.get_voices()
# Chose the desired voice and extract it from the list
sam_voice: Voice = list(filter(lambda x: x.name == 'Sam', all_voices))[0]
# Text to convert
text: str = 'Hello world!'
# Send text to speech conversion request
audio_data: bytes = api.text_to_speech(sam_voice.id, text, stability=0.57, similarity_boost=0.82,
                                       model_id=ModelId.MULTILINGUAL, latency=LatencyOptimization.STRONG)
# Save audio to file
with open('audio.mp3', 'wb') as file:
    file.write(audio_data)
```

After this call is done, you will be able to find the audio file at the specified file. In the console output you should see:

```
[INFO][ElevenLabsApi] Getting available voices
[INFO][ElevenLabsApi] Converting text to speech using voice with ID yoZ06aMxZJJ28mfd3POQ
```

Or when logger is configured to show debug messages:

```
[INFO][ElevenLabsApi] Getting available voices
[INFO][ElevenLabsApi] Converting text to speech using voice with ID yoZ06aMxZJJ28mfd3POQ
[DEBUG][ElevenLabsApi] Stability: 0.57
[DEBUG][ElevenLabsApi] Similarity boost: 0.82
[DEBUG][ElevenLabsApi] Model ID: ModelId.MULTILINGUAL
[DEBUG][ElevenLabsApi] Streaming latency optimization: LatencyOptimization.STRONG
[DEBUG][ElevenLabsApi] Text to convert: Hello world!
```

## <a name="getting_default_voice_settings"></a>Getting default voice settings

In order to get default voice settings, call the `get_default_voice_settings` method. This method returns a `VoiceSettings` object.

```python
from eleven_labs_sdk import ElevenLabsApi, VoiceSettings
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to download default voice settings
default_settings: VoiceSettings = api.get_voice_settings()
# Print settings
print(default_settings)
```

You will see output like this:

```
[INFO][ElevenLabsApi] Getting default settings
VoiceSettings(stability=0.75, similarity_boost=0.75)
```

## <a name="getting_voice_settings"></a>Getting voice settings

In order to download settings for the specific voice, you need a voice ID of the desired voice. Then, call `get_voice_settings` method and pass the voice ID as a parameter. This method returns a `VoiceSettings` object.

```python
from eleven_labs_sdk import ElevenLabsApi, VoiceSettings
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Send request to download voice settings
voice_settings: VoiceSettings = api.get_voice_settings(voice_id)
# Print settings
print(voice_settings)
```

Output:

```
[INFO][ElevenLabsApi] Getting  settings for voice with ID yoZ06aMxZJJ28mfd3POQ
VoiceSettings(stability=0.21, similarity_boost=0.865)
```

## <a name="getting_specific_voice"></a>Getting specific voice

In order to get a specific voice, you need a voice ID of the desired voice. Then, call `get_voice` method and pass the voice ID as a parameter. This method returns a `Voice` object.

```python
from eleven_labs_sdk import ElevenLabsApi, Voice
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Send request to download voice properties
voice: Voice = api.get_voice(voice_id)
```

## <a name="deleting_specific_voice"></a>Deleting specific voice

In order to delete a specific voice, you need an ID of the voice you want to delete. Then, call `delete_voice` method and pass the voice ID as a parameter.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Send request to delete voice
operation_status: str = api.delete_voice(voice_id)
# Print operation status
print(operation_status)
```

## <a name="editing_voice_settings"></a>Editing voice settings

In order to edit voice settings, you need a voice object that you want to edit and object with the new voice settings that you want to assign.

```python
from eleven_labs_sdk import ElevenLabsApi, VoiceSettings
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Create new settings
settings: VoiceSettings = VoiceSettings(stability=0.38, similarity_boost=0.67)
# Edit voice settings
operation_status: str = api.edit_voice_settings(voice_id, settings)
# Print operation status
print(operation_status)
```

## <a name="creating_new_voice"></a>Creating new voice

In order to create a new voice, you need to prepare at least 2 things:
 * name of the new voice
 * list of files containing samples of the new voice

Optionally, you may provide description of the new voice and voice labels, but they may be empty.

```python
voice_id: str = api.add_voice(name='MY_VOICE_NAME', files=[SAMPLE_1, SAMPLE_2], description='VOICE DESCRIPTION', labels='{"label1": "value1", "label2": "value2"}')
```

This method returns ID of the newly created voice.

## <a name="editing_voice"></a>Editing voice

Editing voice is very similar to creating a new voice. The only difference is that you need to provide a voice ID of the voice that you want to edit.

```python
# Choose voice that you want to edit
voice_id: str = 'VOICE_ID'
# Send request to edit the voice
api.edit_voice(voice_id, new_name='MY_NEW_VOICE_NAME', new_samples=[NEW_SAMPLE_1, NEW_SAMPLE_2], new_description='NEW VOICE DESCRIPTION', new_labels='{"label3": "value3", "label4": "value4"}')
```

## <a name="deleting_voice_sample"></a>Deleting voice sample

In order to delete a voice sample, you need to provide a voice object and a sample ID. Then, call `delete_sample` method and pass the voice ID and sample ID as parameters.

```python
# Choose voice ID
voice_id: str = 'VOICE_ID'
# Choose sample ID
sample_id: str = 'SAMPLE_ID'
# Send request to delete the sample
operation_status: str = api.delete_sample(voice_id, sample_id)
# Print status
print(operation_status)
```

## <a name="getting_audio_from_sample"></a>Getting audio from sample

In order to get audio from a sample, you need to provide a voice ID and a sample ID.

```python
# Choose voice that you want to get audio sample from
voice_id: str = 'VOICE_ID'
# Choose sample ID
sample_id: str = 'SAMPLE_ID'
# Send get audio from sample request
audio_data: bytes = api.get_audio_from_sample(voice_id, sample_id)
# Save audio data to file
with open('audio.mp3', 'wb') as file:
    file.write(audio_data)
```

## <a name="getting_generated_items"></a>Getting generated items

In order to get items that you have already generated in the past, use `get_generated_items` method.

```python
from typing import List
from eleven_labs_sdk import ElevenLabsApi, HistoryItem
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to get generated items
history_items: List[HistoryItem] = api.get_generated_items()
# Print history items
print('All history items:')
for item in history_items:
    print(f' * {item}')
```

Depending on the items you have generated on your account, you will see output similar to the output below:

```
[INFO][ElevenLabsApi] Getting generated history items
 * HistoryItem(id='ITEM_ID_1', request_id='REQUEST_ID_1', ...)
 * HistoryItem(id='ITEM_ID_2', request_id='REQUEST_ID_2', ...)
```

## <a name="getting_audio_from_history_item"></a>Getting audio for history item

In order to download audio that you have generated in the past, you need to provide a history item ID.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose ID of a history item to get audio from
history_item_id: str = 'ITEM_ID'
# Send request
audio_data: bytes = api.get_audio_from_history_item(history_item_id)
# Save audio to file
with open('audio.mp3', 'wb') as file:
    file.write(audio_data)
```

## <a name="deleting_history_item"></a>Deleting history item

In order to delete a history item, you need to provide a history item ID that you want to delete. Then, call `delete_history_item` method and pass the history item ID as a parameter.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose ID of a history item to get audio from
history_item_id: str = 'ITEM_ID'
# Send request
operation_status: str = api.delete_history_item(history_item_id)
# Print operation status
print(operation_status)
```

## <a name="downloading_history_items"></a>Downloading history items

With this function, you are able to download one or more audio files from the history items. If you provide only one history item ID, then you can save the audio to an individual media file, but if you provide more than one ID to download, then it should be saved to a .zip file.

```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Choose ID of a history item to get audio from
history_item_id: str = 'ITEM_ID'
# Send request
audio_data: bytes = api.download_history_items([history_item_id])
# Save audio to file
with open('audio.mp3', 'wb') as file:
    file.write(audio_data)
```
```python
from eleven_labs_sdk import ElevenLabsApi
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request
audio_data: bytes = api.download_history_items(['ITEM_ID_1', 'ITEM_ID_2'])
# Save audio to file
with open('audio_files.zip', 'wb') as file:
    file.write(audio_data)
```

## <a name="getting_user_subscription_info"></a>Getting user subscription info

In order to get information about your subscription, use `get_user_subscription_info` method.

```python
from eleven_labs_sdk import ElevenLabsApi, UserSubscriptionInfo
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to get user subscription info
subscription_info: UserSubscriptionInfo = api.get_user_subscription_info()
# Print subscription info
print(subscription_info)
```

## <a name="getting_user_info"></a>Getting user info

In order to get user information, use `get_user_info` method.

```python
from eleven_labs_sdk import ElevenLabsApi, UserInfo
# Create API object
api = ElevenLabsApi(api_key='YOUR_API_KEY')
# Send request to get user subscription info
user_info: UserInfo = api.get_user_info()
# Print user info
print(user_info)
```