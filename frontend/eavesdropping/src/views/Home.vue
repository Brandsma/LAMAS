<template>
  <div class="blog">
    <h1>Introduction</h1>
    <p>
      <span class="first-letter">C</span
      ><it>ommunication is information in motion</it>, the dynamics of which are
      described by the changing knowledge and beliefs for some set of agents.
      Remembering that knowledge is power, agents may wish to carefully control
      the flow of information in a system by way of
      <it>private communication</it>. This proves to be a non-trivial task when
      a third-party agent wishes to <it>eavesdrop</it> on an information
      exchange. The archetypical defense against eavesdropping is
      <it>encryption</it>, whereby the true meaning of messages are disguised by
      an encoding that is uniquely readable to the agent for which a message is
      intended. However, an eavesdropping agent may employ a trick such that
      communicating agents believe they are encoding messages for their partner,
      but instead encode them for the eavesdropper. How then can private
      communication be achieved? Can communicating agents ever know that their
      exchange of information is indeed private?
    </p>
    <p>
      Here we present three cases of "private communication" as outlined, along
      with graphic simulations in the spirit of, and novel epistemic formalism.
      First we illustrate a basic RSA encryption protocol with the case of
      perfect, deletion-error-free communication between two agents, Alice and
      Bob. We then demonstrate how this method is vulnerable to breeches in
      privacy through belief-manipulation with the introduction of an
      eavesdropping agent Eve. Finally, we present the "interlocks" protocol
      [<router-link :to="{ name: 'References' }">2</router-link>] as a solution
      to the eavesdropping, whereby Alice and Bob are guaranteed to become aware
      of the presence of Eve and may therefore cease communication on that
      compromised line.
    </p>
    <p>
      At this point, you may be asking yourself, "Why bother with privacy? I've
      got nothing to hide." Luckily, we may refer you to [<router-link
        :to="{ name: 'References' }"
        >4</router-link
      >], wherein you will find that you indeed do have an interest in
      maintaining privacy whenever possible in personal communication. The need
      for privacy extends much farther than revolutionaries, spies, and
      nefarious agents. <br />
      As aforementioned, knowledge is power. Knowledge
      <it>about</it> us can be wielded as power <it>over</it> us. If we are
      laissez-faire with who can listen in on our communication, then we have no
      way of knowing what their interest in our information might be. From
      targeted advertisement to predicting our behaviour to a deliberate
      shifting of our political views, the more that is known about us, the more
      effectively we may be influenced. The first step in protecting ourselves
      from listeners with unknown intent is to know in what cases we are being
      listened to. When are we in the presence of an Eve?
    </p>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      formula: "",
    };
  },
};
</script>

<style scoped>
.first-letter {
  float: left;
  font-size: 75px;
  line-height: 60px;
  padding-top: 4px;
  padding-right: 8px;
  color: #4caf50;
  padding-left: 3px;
}
</style>
