<template>
  <div class="blog">
    <h2>{{ $route.name }}</h2>
    <p>
      Protocol verification procedures are an essential mechanism for
      distributed systems, whereby two processors can reach a state of shared
      knowledge that a piece of information has certainly been transferred,
      which is a prerequisite to the next bit of information being passed.
      Already, such a system is subject to deletion errors of moving bits and
      therefore the approach to achieve secure communication becomes rather
      nuanced, requiring fourth-order higher-knowledge. Abstracting away from
      distributed systems, a similar formalism may be adopted for any form of
      communication which is intended to be secure. The consideration of one
      agent passing a string of information (such as a password) to another can
      thus be modeled with a number of additional caveats that may interfere
      with their simple goal. Here the influence of a third agent--<i
        >the eavesdropper</i
      >--on private communication is investigated. In order to do this, first a
      base model demonstrating standard communication protocols is presented
      along with the associated formalism and Kripke structures. Next, a novel
      eavesdropping agent is introduced to the system, which will intercept
      passing bits of information with a given frequency and publicly announce
      its stolen data. <b>[Two possibilities:]</b>
    </p>

    <ol>
      <li>
        With this public announcement, the two communicating agents will
        determine if the eavesdropping agent has attained sufficient information
        to justify their re-initializing exchange. \hl{(more difficult)} \item
        It is shown that the baseline protocol is not equipped for private
        communication with the presence of an eavesdropper. Therefore, a novel
        expansion is proposed to fortify privacy in communication. It is then
        modeled and presented with appropriate formalism and key Kripke
        structures. <b>more practical</b>
      </li>
    </ol>

    <h2>Baseline Protocol</h2>
    <p>
      The transfer of a password bit-by-bit can from one agent to another can be
      treated as an instantiation of protocol verification, as found in
      distributed systems \hl{[citation]}, the archetypical variation of which
      may be referred to as \textit{protocol A} as described in \hl{[text-book
      citation]}. Qualitatively, the procedure is as follows: The sender learns
      the first bit of the password ($A$ for example) and sends it to the
      receiver repeatedly. Once a bit makes it through, the receiver writes the
      bit to its own password tape and returns a bit repeatedly stating that it
      knows the bit ($K_rA$). Once the sender receives ($K_rA$), it stops
      sending ($A$) bits and starts sending ($K_sK_rA$) bits, acknowledging that
      the the sender knows the receiver knows the initial bit. When the receiver
      receives ($K_sK_rA$), it stops sending ($K_rA$) bits and starts sending
      ($K_rK_sK_rA$) bits. Finally, once the sender receives a ($K_rK_sK_rA$)
      bit, it can be sure its initial bit has been correctly received
      ($K_sK_rK_sK_rA$). Now the sender may stop sending ($K_sK_rA$) and start
      sending the next bit from the password. \hl{[include psuedo code from text
      book?]} Notice this protocol is safe from something like deletion errors.
      Information is continually sent by one agent until it receives
      confirmation from its partner agent that its information has been
      received. While this protocol indeed guarantees that a complete string of
      information can be shared correctly, it does nothing to ensure this
      information is being passed \textit{securely}.
      <img src="../assets/img/kripke_A.png" alt="This is the kripke A model" />
    </p>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped>
</style>
