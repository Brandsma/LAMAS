

# Encrypted communication protocols with eavesdropping and eavesdrop detection.

Logical Aspects of Multi-Agent Systems 2021 Project -- *Abe Brandsma, Ryan O'Laughlin, Ivo Steegstra*

Overview of the model
---------------------
The model mainly consists of a communication framework between two agents, originally based on the LOKWebs assignments.
Two agents communicate messages through a channel which they do not operate. Agents send confirmation messages up until
the confirmation depth is achieved, at which point they know that the other has received knowledge of an order which is satisfactory.
From this base many features are added; communication using encryption, two-way communication, eavesdropping, the eavesdrop detecting 
interlock protocol, and any (theoretically possible) permutation of these features.

The design of the model places a high priority on modularity and sound architecture. This is made apparent by the ease of integration
between the different modes of operation.

Thoughout the model care is taken to comment where explanation of the model is required. Comments are often notes for the programmer, 
but also do a good job explaining the why of a piece of code to the technical reader.


Model entities
--------------
```
Process : The highest level entity, used mainly to keep track of the order of events using Lamports time algorithm for distributed systems. (I would have loved to upgrade to vector clocks, but priorities lay elsewhere)

    Channel : A one-way communication channel facilitating communication between agents. Modular design using buffers.

    Agent : A communicating entity -- capable of message handling, connecting with channels, encryption and interlock protocols, different reporters.
        Sender : A subtype of an agent harbouring the capabilties of producing, sending and acknowledging messages.
        Receiver : A subtype of an agent harbouring the capabilities of receiving and acknowledging messages.
            Communicator : A subtype of an agent inheritting from both Sender and Receiver, used for two-way communication

    Eavesdropper : Eavesdropper process, utilizing two agents spoofing connection to the 'real' communicators. Real Alice meet Fake Bob, Real Bob meet Fake Alice.

    Message : An object used as communication vessel.

Stepper : Controlling entity scheduling when which process acts. 
```

Basic model loop
----------------

The stepper controls which process acts at which point. It does so sequentially.
A sending agent prepares their message they want to send by placing it in their outgoing buffer. The message is moved from their
outgoing buffer to the incomming buffer of their outgoing-connected channel. From there it is moved to that channels 'chute',
which then transfers the message to its outgoing buffer. From there the message is moved to the incomming buffer of the receiving agent.
The receiving agent reads the message, decides whether or not to acknowledge the message (and place it in their own outgoing buffer), to store the message,
or to respond with their own message (two-way communication). The process is repeated symetrically using a different channel.

When there is an eavesdropper in the model, it hijacks the communication channels and places its own spoofed agents on either side.
This means there are now four communication channels instead of two.
The eavesdropper transfers messages received on one side to the other side, to give the illusion the unknowing agents are speaking to eachtoher
without anyone listening.

With encryption, agents first produce their private/public key pair and exchange public keys. They will encrypt their outgoing messages with the public key
received from the other party, and decrypt incomming ciphertext with their own private key. The encryption algorithm used is RSA. Encryption is applied
when transfering their message from their output buffer to the channels input buffer.

With the interlock protocol, agents split their outgoing message (after encryption) when transfering their message from their output buffer to
their outgoing channels input buffer. A message is split in half, the remaining half is stored and sent (only) after receiving a new message (that is not an acknowledge)
by the other party.



How to run the program (basic):
-------------------------------
(If required install the following packages / dependencies: logger, rsa)
```bash
run "python main.py"
```
The program now asks to run either of three scenarios:

1 - Perfect Communication

2 - Perfect Communication With Eavesdropping

3 - The Interlock Protocol

Then the program asks whether or not to include encryption and if the communication should be one or two-ways.


"What is the output?":
----------------------
The output of the model shows the messages each agent has in their sending and receiving list,
both at the start and the end of the model. This shows that the model is working properly and messages intended
to send are sent and received. It also shows that the eavesdropper knows the messages.
A highly detailed log of what happens can be enabled by setting "print_log_to_terminal" and/or "print_channel_content"
to true in the config.py file.
Note that when encryption is turned on, output can be more messy, as encryption keys and encrypted texts are long and machine-readable.


How to change the model / experiment with settings:
--------------------------------------------------
To use your own config, set the commandline_config_chooser value in the config.py file to False

Most of the relevant settings can be found in the "config.py" file.
At the top of this file the reader will find many switches for different modes of running the program:
- encryption_protocol   (Will agents use encryption when communicating?)
- include_eavesdropper  (Is there an eavesdropper through which the agents communicate?)
- two_way_communication (Is communication one or two way? Two way means both send and receive message content. One-way still includes acknowledges from the receiver)
- interlock_protocol    (Is the interlock protocol employed in communication?)

As well as operating parameters:
- stepper_time_limit    (How many steps the program will take, recommended to keep at 300+ to see a full execution)
- message_timeout       (How long an agent waits before resending a message -- setting to a value other than 1 can produce strange behaviour)
- acknowledge_depth     (The number of acknowledges required in total -- can be seen as the "order of theory of mind-level" parameter, recommended to read the warning messages below before changing.)

Some failure model parameters, not yet properly implemented (but can be done with easy, if the instructor of the course is interested in a better version of the LOKwebs model ;) --> contact Ivo)

Some output parameters:
- save_log_to_file      (Save a log trace of all actions/states to file, used for the animations)
- print_log_to_terminal (Print the log trace of all actions to the terminal, for debugging and inspection)
- print_channel_content (Print the channel content at certain moments to the terminal. Not as expressive as the log trace, but more easy to read)
- loglevel              (Log statements thoughout the model, can be set at logging.DEBUG for most expressive, then logging.INFO, 
                        logging.WARNING, logging.ERROR for least expressive)

How to run the mode (advanced):
-------------------------------
The model runs from the file main.py, which calls the communication_demo.py file.
This file describes the protocol that is initiated for a single run. The advanced user can observe the order components
initialized and invoked here. Changes in here should be limited to changing the message content and switching connections.
For any really advanced changes, reading the documentation of the structure and entities is strongly recommended. 


"Why does this not work?"
-------------------------
Certain parameter combinations are theoretically incongruent. Most notably:

- an uneven value for the acknowledge_depth parameter is required for one-way communication
- an even value for the acknowledge_depth parameter is required for two-way communication
- a value of 0 for the acknowledge_depth parameter is required for the interlock_protocol
- the interlock_protocol requires two-way communication
- (!) the interlock_protocol combined with the eavesdropper will result in a decryption error


Note about the logic folder
---------------------------
The logic folder houses some code that was intended to be used for knowledge representation in the model and includes an automatic solver for S5-like models.
During the project, we decided that the knowledge-side of the project was more suited to be modelled statically. 
This can be found on the website under the 'Formalism' section.