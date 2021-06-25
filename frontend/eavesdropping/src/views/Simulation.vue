<template>
  <div class="blog">
    <h1>Simulation</h1>
    <p>
      This page gives a description of the simulation below, as well as the link
      to the code itself. The code needs to be run on your own computer and
      cannot be run in this browser.
    </p>

    <a
      href="https://github.com/Brandsma/LAMAS"
      target="_blank"
      rel="noopener noreferrer"
      ><button class="github-button">
        <div class="button-content">
          <img
            style="width: 20%"
            src="https://img.icons8.com/fluent/48/000000/github.png"
          />Project Code
        </div>
      </button></a
    >

    <p>
      <button
        type="button"
        v-on:click="toggleCollapsible"
        :class="{ collapsible: true, active: isShowingCollapsible }"
      >
        Show Project README
      </button>
    </p>
    <div
      :class="{
        content: !isShowingCollapsible,
        'content-not-hidden': isShowingCollapsible,
      }"
    >
      <h2>Overview of the model</h2>

      <p>
        The model mainly consists of a communication framework between two
        agents, originally based on the LOKWebs assignments. Two agents
        communicate messages through a channel which they do not operate. Agents
        send confirmation messages up until the confirmation depth is achieved,
        at which point they know that the other has received knowledge of an
        order which is satisfactory. From this base many features are added;
        communication using encryption, two-way communication, eavesdropping,
        the eavesdrop detecting interlock protocol, and any (theoretically
        possible) permutation of these features.
        <br />
        The design of the model places a high priority on modularity and sound
        architecture. This is made apparent by the ease of integration between
        the different modes of operation.

        <br />
        Thoughout the model care is taken to comment where explanation of the
        model is required. Comments are often notes for the programmer, but also
        do a good job explaining the why of a piece of code to the technical
        reader.
      </p>

      <h2>Model entities</h2>
      <pre>
Process : The highest level entity, used mainly to keep track of the order of events using Lamports time 
          algorithm for distributed systems. (I would have loved to upgrade to vector clocks, 
          but priorities lay elsewhere)

    Channel : A one-way communication channel facilitating communication between agents. 
              Modular design using buffers.

    Agent : A communicating entity -- capable of message handling, connecting with channels, encryption 
            and interlock protocols, different reporters.
        Sender : A subtype of an agent harbouring the capabilties of producing, sending and 
                 acknowledging messages.
        Receiver : A subtype of an agent harbouring the capabilities of receiving and 
                   acknowledging messages.
            Communicator : A subtype of an agent inheritting from both Sender and Receiver, used for 
                           two-way communication

    Eavesdropper : Eavesdropper process, utilizing two agents spoofing connection to the 'real' 
                   communicators. Real Alice meet Fake Bob, Real Bob meet Fake Alice.

    Message : An object used as communication vessel.

Stepper : Controlling entity scheduling when which process acts. 
</pre
      >

      <h2>Basic model loop</h2>

      <p>
        The stepper controls which process acts at which point. It does so
        sequentially. A sending agent prepares their message they want to send
        by placing it in their outgoing buffer. The message is moved from their
        outgoing buffer to the incomming buffer of their outgoing-connected
        channel. From there it is moved to that channels 'chute', which then
        transfers the message to its outgoing buffer. From there the message is
        moved to the incomming buffer of the receiving agent. The receiving
        agent reads the message, decides whether or not to acknowledge the
        message (and place it in their own outgoing buffer), to store the
        message, or to respond with their own message (two-way communication).
        The process is repeated symetrically using a different channel. When
        there is an eavesdropper in the model, it hijacks the communication
        channels and places its own spoofed agents on either side. This means
        there are now four communication channels instead of two. The
        eavesdropper transfers messages received on one side to the other side,
        to give the illusion the unknowing agents are speaking to eachtoher
        without anyone listening. With encryption, agents first produce their
        private/public key pair and exchange public keys. They will encrypt
        their outgoing messages with the public key received from the other
        party, and decrypt incomming ciphertext with their own private key. The
        encryption algorithm used is RSA. Encryption is applied when transfering
        their message from their output buffer to the channels input buffer.
        With the interlock protocol, agents split their outgoing message (after
        encryption) when transfering their message from their output buffer to
        their outgoing channels input buffer. A message is split in half, the
        remaining half is stored and sent (only) after receiving a new message
        (that is not an acknowledge) by the other party.
      </p>
      <h2>How to run the program (basic):</h2>

      <pre class="code">
run "python main.py"
</pre
      >

      <h2>"What is the output?":</h2>
      <p>
        The output of the model shows the messages each agent has in their
        sending and receiving list, both at the start and the end of the model.
        This shows that the model is working properly and messages intended to
        send are sent and received. It also shows that the eavesdropper knows
        the messages. A highly detailed log of what happens can be enabled by
        setting "print_log_to_terminal" and/or "print_channel_content" to true
        in the config.py file.<br />
        Note that when encryption is turned on, output can be more messy, as
        encryption keys and encrypted texts are long and machine-readable.
      </p>

      <h2>How to change the model / experiment with settings:</h2>

      <p>
        Most of the relevant settings can be found in the "config.py" file. At
        the top of this file the reader will find many switches for different
        modes of running the program:
      </p>
      <ul>
        <li>
          encryption_protocol (Will agents use encryption when communicating?)
        </li>
        <li>
          include_eavesdropper (Is there an eavesdropper through which the
          agents communicate?)
        </li>
        <li>
          two_way_communication (Is communication one or two way? Two way means
          both send and receive message content. One-way still includes
          acknowledges from the receiver)
        </li>
        <li>
          interlock_protocol (Is the interlock protocol employed in
          communication?)
        </li>
      </ul>

      <p>As well as operating parameters:</p>
      <ul>
        <li>
          stepper_time_limit (How many steps the program will take, recommended
          to keep at 300+ to see a full execution)
        </li>
        <li>
          message_timeout (How long an agent waits before resending a message --
          setting to a value other than 1 can produce strange behaviour)
        </li>
        <li>
          acknowledge_depth (The number of acknowledges required in total -- can
          be seen as the "order of theory of mind-level" parameter, recommended
          to read the warning messages below before changing.)
        </li>
      </ul>

      <p>
        Some failure model parameters, not yet properly implemented (but can be
        done with easy, if the instructor of the course is interested in a
        better version of the LOKwebs model ;) --> contact Ivo)
      </p>

      <p>Some output parameters:</p>
      <ul>
        <li>
          save_log_to_file (Save a log trace of all actions/states to file, used
          for the animations)
        </li>
        <li>
          print_log_to_terminal (Print the log trace of all actions to the
          terminal, for debugging and inspection)
        </li>
        <li>
          print_channel_content (Print the channel content at certain moments to
          the terminal. Not as expressive as the log trace, but more easy to
          read)
        </li>
        <li>
          loglevel (Log statements thoughout the model, can be set at
          logging.DEBUG for most expressive, then logging.INFO, logging.WARNING,
          logging.ERROR for least expressive)
        </li>
      </ul>

      <h2>How to run the modes manually (advanced):</h2>
      <p>
        The model runs from the file main.py, which calls the
        communication_demo.py file. This file describes the protocol that is
        initiated for a single run. The advanced user can observe the order
        components initialized and invoked here. Changes in here should be
        limited to changing the message content and switching connections. For
        any really advanced changes, reading the documentation of the structure
        and entities is strongly recommended.
      </p>

      <h2>"Why does this not work?"</h2>
      <p>
        Certain parameter combinations are theoretically incongruent. Most
        notably:
      </p>

      <ul>
        <li>
          an uneven value for the acknowledge_depth parameter is required for
          one-way communication
        </li>
        <li>
          an even value for the acknowledge_depth parameter is required for
          two-way communication
        </li>
        <li>
          a value of 0 for the acknowledge_depth parameter is required for the
          interlock_protocol
        </li>
        <li>the interlock_protocol requires two-way communication</li>
        <li>
          (!) the interlock_protocol combined with the eavesdropper will result
          in a decryption error
        </li>
      </ul>

      <h2>Note about the logic folder</h2>

      <p>
        The logic folder houses some code that was intended to be used for
        knowledge representation in the model and includes an automatic solver
        for S5-like models. During the project, we decided that the
        knowledge-side of the project was more suited to be modelled statically.
        This can be found on the website under the 'Formalism' section.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Simulation",
  data() {
    return {
      isShowingCollapsible: false,
    };
  },
  methods: {
    toggleCollapsible: function () {
      this.isShowingCollapsible = !this.isShowingCollapsible;
    },
  },
};
</script>

<style style="scss" scoped>
pre {
  width: 100%;
  background-color: #e1e1e1;
  color: black;
  padding: 10px;
}

.github-button {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 12px;
  background: white;
  border: 2px solid #2c3e50;
  margin: 20px;
}

.github-button:hover {
  background: #f0f0f0;
  cursor: pointer;
}

.button-content {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin: 6px;
  text-decoration: none;
}

.collapsible {
  display: flex;
  justify-content: center;
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active,
.collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0.5em 6em;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}

.content-not-hidden {
  padding: 0.5em 6em;
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f1f1f1;
}
.content-not-hidden > p {
  width: 70%;
}
.content-not-hidden > ul {
  width: 60%;
}

.content-not-hidden > ol {
  width: 60%;
}
</style>
