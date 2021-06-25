<template>
  <div class="blog">
    <h1>{{ $route.name }}</h1>
    <h2>Perfect Communication - S5 Model</h2>
    <p>
      Let us now abstract to the simplest scenario where Alice has only two
      possible public keys, and Bob has only two possible messages to
      communicate with Alice. Realize that the fundamental logic of this
      abstraction holds symmetrically for communication in the opposite
      direction, as well as iterativily for any number of possible keys and
      messages. In fact, we invite you to imagine that the first possible public
      key for Alice represents her actual key, and the second key stands in for
      <it>all possible other keys</it>. Likewise, please think of Bob's first
      possible message as his actual message, and the second possible message as
      all possible other messages. The logic and relations work the same whether
      these secondary keys and messages are inductively expanded or collapsed.
      For a similar example of "inductive collapse", we refer the reader to
      [<router-link :to="{ name: 'References' }">1</router-link>]. As a final
      note, the reflexivity relationships have not been drawn for simplicity's
      sake.
    </p>

    <p>
      In the first figure below, we may see the epistemic states unfold for this
      simplified communication, where there are only two possible public keys
      for Alice (
      <math-jax :formula="'$pubA1$'"></math-jax>
      and
      <math-jax :formula="'$pubA2$'"></math-jax>
      ), and two possible messages Bob might send (<it>p</it> and <it>q</it>).
    </p>

    <p>
      Here we assume that in the initial state (top-left in the figure), Alice
      knows her key and Bob knows the message he wants to send. Therefore, Alice
      cannot distinguish between
      <math-jax :formula="'$mBp$'"></math-jax> and
      <math-jax :formula="'$mBq$'"></math-jax>, while Bob cannot distinguish
      between <math-jax :formula="'$pubA1$'"></math-jax> and
      <math-jax :formula="'$pubA2$'"></math-jax>. This is described by the
      appropriate accessibility relations which indicate which worlds must be
      simultaneously accepted as possible for a given agent. Note, all worlds
      have reflexive relations for all agents and that these are
      <it>S5-Kripke structures.</it>
    </p>

    <p>
      Once Bob receives Alice's public key, Bob now knows whether it is
      <math-jax :formula="'$pubA1$'"></math-jax> or
      <math-jax :formula="'$pubA2$'"></math-jax>. He cannot accept both of these
      states as simultaneously true and therefore all accessibility relations
      between the two possible public keys drop out. Now that
      <math-jax :formula="'$K_B pubA$'"></math-jax>, Bob may correctly encrypt
      his message (either <math-jax :formula="'$mBp$'"></math-jax> or
      <math-jax :formula="'$mBq$'"></math-jax>) and send it to Alice.
    </p>

    <img src="@/assets/img/perf_kripke.png" alt="Image perf_kripke" />

    <p>
      Alice then receives Bob's message and decrypts it with her private key,
      finally alleviating any remaining indistinguishability. Thus information
      has been fruitfully shared and everyone knows everything. While this type
      of model does show each state correctly, it does not give a clear
      representation of the steps that are taken in between. It is also not a
      prerequisite for the model to first have received the key before sending
      the message. These issues will be resolved with action models.
    </p>

    <h2>Perfect Communication - Action Model</h2>

    <p>
      Here we present the first action model. Before getting into the details of
      the situation at hand, there are a few important distinctions to be noted
      for all action models that we present. First of all, the
      <it>true</it> world is represented by a thick line. Secondly, the kripke
      structures that are shown here are no longer
      <it>S5-Kripke structures</it>, but rather
      <math-jax :formula="'$\\mathbb{L}_{KC\\otimes}$'"></math-jax> , which
      includes everything from <it>S5</it> and in addition adds the concept of
      <it>actions</it>. For more information about this subject, see
      [<router-link :to="{ name: 'References' }">3</router-link>].
    </p>

    <p>
      Now back to communicating. In the initial state, we assume Bob knows which
      message he will send and Alice knows which key is hers. Logically, there
      are two possible keys for Bob to receive, but in reality there is only one
      (A1). His reception of the key defines the first action of the model and
      results in the new Kripke model on the right.
    </p>

    <math-jax :formula="'$$E = \\{BrA1, BrA2\\}$$'"></math-jax>

    <math-jax
      :formula="'$$R_A=\\{(e1,e2)| (mBp \\in e1)\\wedge (mBq \\in e2)\\}$$'"
    ></math-jax>
    <math-jax :formula="'$$R_B= E \\times E$$'"></math-jax>
    <math-jax :formula="'$$\\textnormal{pre}(BrA1)=A1$$'"></math-jax>
    <math-jax :formula="'$$\\textnormal{pre}(BrA2)=A2$$'"></math-jax>

    <img
      src="@/assets/img/perfect_communication_1.jpg"
      alt="Image perfect_communication_1"
    />

    <p>
      The second action in the protocol whereby Bob sends his message and Alice
      receives defines the preconditions
      <math-jax :formula="'$\\textnormal{pre}(ArmBp)=mBp$'"> </math-jax> and
      <math-jax :formula="'$\\textnormal{pre}(ArmBq)=mBq$'"></math-jax>
      which result in the union visualized in the final Kripke structure on the
      right.
    </p>

    <math-jax :formula="'$$E = \\{ArmBp, ArmBq\\}$$'"> </math-jax>
    <math-jax :formula="'$$R_A = E \\times E$$'"> </math-jax>
    <math-jax :formula="'$$R_B=\\{(e,e)| e \\in E\\}$$'"></math-jax>
    <math-jax :formula="'$$\\textnormal{pre}(ArmBp)=mBp$$'"> </math-jax>
    <math-jax :formula="'$$\\textnormal{pre}(ArmBq)=mBq$$'"> </math-jax>
    <img
      style=""
      src="@/assets/img/perfect_communication_2.jpg"
      alt="Image perfect_communication_2"
    />
    <div class="CENTER"></div>

    <h2>Eavesdropping</h2>

    <h3>S5 Model</h3>

    <p>
      In terms of epistemic logic, we now see certain nuances emerge. What is of
      special interest is the false belief that Alice and Bob have concerning
      whose public key they receive. Again, we can consider the simplified case
      of Alice sending one of two possible public keys, and Bob sending one of
      two possible messages. Again, the logic derived here can be extended to an
      infinite number of possible keys and messages by induction. Note that
      Eve's public key is also modelled, but only as one possible key. However,
      this can also be expanded by induction to arbitrarily many public keys.
      Please note that these step-by-step Kripke models fail to model key
      ownership as perceived by Bob. In order to incorporate Eve's deception of
      Bob formally, action models will be needed and are included in the next
      section.
    </p>

    <p>
      Considering the figure below with the S5 kripke models from left-to-right,
      and then downward:
    </p>

    <ul>
      <li>
        In the initial state, Bob can distinguish between no public keys and
        thus must consider all key nodes simultaneously possible through
        accessibility relations. Bob does know the content of his own
        prospective message however, and so there are no lateral relations for
        Bob between possible messages. While Alice cannot distinguish between
        possible messages of Bob, she does know the difference between her own
        possible keys and Eve's key and therefore has no accessibility relations
        between these nodes. Eve can only discern a difference between her own
        public key and Alice's public key at this point, and must accept all
        other possibilities at this point in time.
      </li>
      <li>
        After Eve receives Alice's public key she can now drop the accessibility
        relations between Alice's possible keys.
      </li>
      <li>
        Once Bob receives Eve's public key (thinking that it is Alice's), all
        key worlds become mutually exclusive for Bob as well.
      </li>
      <li>
        Upon receiving and decrypting Bob's message, Eve now may distinguish all
        possible message nodes.
      </li>
      <li>
        Once Alice finally receives Bob's message (encrypted with Eve's key),
        she can decrypt it with what she thinks is Bob's public key (though it
        is Eve's) and finally, everyone may distinguish all possible states and
        the information is shared.
      </li>
    </ul>

    <p>
      The obvious issue with this situation is that Alice and Bob may very well
      wish to keep there information private.
    </p>

    <img src="@/assets/img/perf_eve_kripke.png" alt="Image perf_eve_kripke" />

    <h3>Action Model</h3>

    <p>
      The introduction of an eavesdropper greatly expands the epistemic dynamics
      of the system, and in fact modelling the caveat that Bob believes he has
      Alice's key when he truly has Eve's key expands the combinatorics of the
      Kripke structures to an infeasible degree if full nodal representation
      would be kept. We therefore again rely heavily on "inductive collapse"
      whereby we may assume that all possible keys are contained in a single
      nodal representation of that key, mainly focusing on the actual keys of
      Alice, Bob, and Eve. Besides message <it>p</it>, we will maintain the
      extra possible message <it>q</it> (standing in for all possible messages
      besides the actual message) to aid in understanding the development of the
      agents their knowledge. Furthermore, realize we are again confining our
      model to the unidirectional circumstance of Bob wanting to get a message
      to Alice. By symmetry, this could of course define the same logic as the
      other way around&ndash;just swap the names.
    </p>

    <ul>
      <li>
        In the initial state (refer to the correct pictures), we have only two
        nodes, both contain the two public keys involved in the system (Alice's
        and Eve's) and otherwise being split between Bob's two possible message
        <it> p </it> (his real message) or <it> q </it> (all other possible
        messages). On this initial state, the action-point
        <math-jax :formula="'$ErA$'"></math-jax>, related to the initial model
        by the precondition
        <math-jax :formula="'$\\textnormal{pre}(ErA) = pubA$'"></math-jax>
        , holds at every node and therefore the action-point is added to each
        node, resulting the new kripke model with action-points
        <math-jax :formula="'$ErA$'"></math-jax>
        Intuitively, this establishes that in all possible worlds, Eve has
        received Alice's public key.
      </li>

      <li>
        From the newly derived Kripke model, we again model an event that will
        change our kripke structure. The action points here are Bob either
        receiving Alice's key or Eve's key (
        <math-jax :formula="'$BrA$'"></math-jax>
        or
        <math-jax :formula="'$BrE$'"></math-jax>
        both of which are defined by the precondition of those keys existing,
        such that
        <math-jax :formula="'$\\textnormal{pre}(BrA) = pubA$'"></math-jax>
        and
        <math-jax :formula="'$\\textnormal{pre}(BrE) = pubE$'"></math-jax>.
        Importantly, Alice and Bob cannot possibly distinguish between these two
        actions points, and therefore their accessibility relations between
        these two possibilities creates a new model dimension, resulting in the
        new Kripke structure, with separate pairs of nodes for Bob either having
        Alice's key or Eve's key.
      </li>

      <li>
        The next event simply adds the action points by which Eve receives Bob's
        message (
        <math-jax :formula="'$ErmBp$'"></math-jax>
        and
        <math-jax :formula="'$ErmBq$'"></math-jax>), with preconditions
        <math-jax :formula="'$\\textnormal{pre}(ErmBp) = pubE, mBp$'">
        </math-jax>
        and
        <math-jax :formula="'$\\textnormal{pre}(ErmBq) = pubE, mBq$'">
        </math-jax>
        thereby removing her accessibility relations between all worlds
        separated only by
        <math-jax :formula="'$mBp$'"></math-jax>
        and
        <math-jax :formula="'$mBq$'"></math-jax>
        These action points are still indistinguishable by Alice, so her
        accessibility relations remain.
      </li>

      <li>
        Finally, Alice receives Bob's message (as passed through Eve) and thus
        the action points
        <math-jax :formula="'$ArmBp$'"></math-jax>
        and
        <math-jax :formula="'$ArmBq$'"></math-jax>
        are added with no accessibility relations, thus breaking the finally
        horizontal accessibility relations of model&ndash;meaning that all
        agents have learned Bob's message. We can form similar preconditions
        here as for the previous event, namely
        <math-jax :formula="'$\\textnormal{pre}(ArmBq) = pubA, mBq$'">
        </math-jax>
        and
        <math-jax :formula="'$\\textnormal{pre}(ArmBq) = pubA, mBq$'">
        </math-jax>
      </li>
    </ul>

    <p>
      Thus, with the aid of action models, we have modelled the important fact
      that while Bob's information is successfully passed, Bob and Alice never
      become aware of the difference between Eve's public key and Alice's.
      Therefore, Eve may successfully and discretely eavesdrop on all of Alice
      and Bobs' communication.
    </p>

    <img src="@/assets/img/eavesdropping_1.jpg" alt="Image eavesdropping_1" />
    <div class="CENTER"></div>

    <img src="@/assets/img/eavesdropping_2.jpg" alt="Image eavesdropping_2" />
    <div class="CENTER"></div>

    <img
      class="final-step"
      src="@/assets/img/eavesdropping_3.jpg"
      alt="Image eavesdropping_3"
    />
    <div class="CENTER"></div>

    <h2 id="interlock-anchor">The interlock protocol</h2>

    <h3>Action Model</h3>

    <p>
      While the protocol seems to increase in complexity, the associated
      formalism barely does. Many of the events are similar when compared to the
      previous two situations that we have shown, the main difference being that
      more messages are being sent <it>and</it> that the full message is not
      know until later. The fact that the full message is not known until later
      makes this a very epistemically interesting situation. We can see this
      clearly in an action model. This time we will only show the action model
      as it may be clear by now that the usual <it>S5</it> worlds do not suffice
      to capture the nuances of eavesdropping. As before, we have two separate
      messages, message <it>p</it> and message <it>q</it> and two separate keys
      <math-jax :formula="'$pubA$'"></math-jax>
      and
      <math-jax :formula="'$pubE$'"></math-jax>. The messages are now broken up
      into two parts and the content of half a message cannot be properly
      deciphered (due to cryptographic reasons). Both halves of <it>p</it> are
      needed in order to <it>know</it> the content of message <it>p</it>. The
      simple addition of breaking the message up into two parts helps the agents
      discern whether or not there is an eavesdropper in the mix as was
      explained in the
      <router-link :to="{ name: 'Methods' }">methods</router-link> section. We
      use one simplification in the modelling of this situation. Usually, the
      interlock protocol requires two-way communication, otherwise Bob would not
      know when to send the next part of the message. If Bob simply follows the
      first message directly by the second, then Eve can simply wait for the
      second half to arrive. We assume that Eve does not use this stalling
      tactic here and simply sends the message on directly.
    </p>

    <p>We can now walk through each step of the protocol using action logic:</p>

    <p></p>

    <ul>
      <li>
        In the initial state, (refer to correct pictures) there are two nodes
        that differ based on the possible message to be sent by Bob (denoted by
        the prepositions
        <math-jax :formula="'$mBp$'"></math-jax>
        and
        <math-jax :formula="'$mBq$'"></math-jax>, read "message p from Bob").
        Alice and Eve are unable to distinguish between these worlds in the
        first step, because they have not received any messages yet. The event
        <math-jax :formula="'$ErA$'"></math-jax>
        (read "Eve receives pubA") is linked to both nodes through the
        precondition
        <math-jax :formula="'$\\textnormal{pre}(ErA)=pubA$'"> </math-jax>
      </li>
      <li>
        After Eve receives Alice her public key, she sends Bob one of the keys
        she has in possession. This can be her own or Alice her key. She chooses
        to send her own key, because that makes it possible to eavesdrop. Both
        actions are dependent on the preconditions
        <math-jax :formula="'$\\textnormal{pre}(BrA)=pubA$'"> </math-jax>
        and
        <math-jax :formula="'$\\textnormal{pre}(BrE)=pubE$'"> </math-jax>. Alice
        and Bob are both unable to discern between which key has been sent.
        Alice has no idea which key was sent and Bob is unable to discern the
        difference, so he believes it to be Alice her key. This adds extra
        dimensionality to the model, because of extra uncertainty relationships.
      </li>
      <li>
        The model that follows from the previous step is the point where the
        keys have been fully exchanged. Now the messages can be sent. The first
        half of the message is being sent (which is represented by
        <math-jax :formula="'$ErmBp[0]$'"></math-jax>, read "Eve receives
        message p[0] from Bob"). There are two distinct actions
        <math-jax :formula="'$ErmBp[0]$'"></math-jax>
        and
        <math-jax :formula="'$ErmBq[0]$'"></math-jax>, and the associated
        preconditions
        <math-jax :formula="'$pre(ErmBp[0]) = pubE, mBp$'"> </math-jax>
        and
        <math-jax :formula="'$pre(ErmBq[0]) = pubE, mBq$'"> </math-jax>. These
        preconditions link it to the correct worlds in the Kripke model.
      </li>
      <li>
        This step is much the same as the previous step, but now Alice receives
        the message. There are technically two options for Eve here. She can
        either send the message Bob send, which Alice cannot decrypt due to
        having the wrong key. Or she can make up her own message, which is most
        likely not going to be the same as Bob's message. To model Alice
        receiving half the message from Bob (unaltered), we can use
        <math-jax :formula="'$pre(ArmBp[0]) = pubA, mBp$'"> </math-jax>
        and
        <math-jax :formula="'$pre(ArmBq[0]) = pubA, mBq$'"> </math-jax>
      </li>
      <li>
        Now Bob sends the second part of the message. This is the first part
        where some accessibility relationships start changing and agents start
        to learn information. Once Eve receives Bob's second message, she will
        know
        <math-jax :formula="'$mBp$'"></math-jax>
        meaning she can distinguish between the worlds with
        <math-jax :formula="'$mBp$'"></math-jax>
        and
        <math-jax :formula="'$mBq$'"></math-jax>. The prepositions
        <math-jax :formula="'$ErmBp[1]$'"></math-jax>
        and
        <math-jax :formula="'$ErmBq[1]$'"></math-jax>
        is added to the model with the preconditions
        <math-jax :formula="'$pre(ErmBp[1]) = pubE, mBp$'"> </math-jax>
        and
        <math-jax :formula="'$pre(ErmBq[1]) = pubE, mBq$'"> </math-jax>.
      </li>
      <li>
        Now Alice receives the second part of the message from Eve as she tries
        to remain transparent to avoid detection. The actions are much the same
        with
        <math-jax :formula="'$pre(ArmBp[1]) = pubA, mBp$'"> </math-jax>
        and
        <math-jax :formula="'$pre(ArmBq[1]) = pubA, mBq$'"> </math-jax>. There
        is one important caveat here though. Since the message was encrypted
        with Eve's public key and not Alice her public key, Alice is now unable
        to decrypt the message. She is unable to read the contents of the
        message, so therefore she cannot distinguish between those worlds. But
        she does know that a different public key was used to encrypt the
        message, which implies that there is an eavesdropper in the middle. This
        leads us to the final kripke model.
      </li>
    </ul>

    <p>
      We can see that the action model does not actually become much more
      complex than before. It is a relatively simple protocol that leads to
      interesting epistemic results, because the final kripke model is
      significantly different than with eavesdropping. So, are we now in the
      presence of an Eve? Indeed, it seems so.
    </p>

    <img style="" src="@/assets/img/interlock_1.jpg" alt="Image interlock_1" />
    <img style="" src="@/assets/img/interlock_2.jpg" alt="Image interlock_2" />
    <img style="" src="@/assets/img/interlock_3.jpg" alt="Image interlock_3" />
    <img
      class="final-step"
      src="@/assets/img/interlock_4.jpg"
      alt="Image interlock_4"
    />
  </div>
</template>

<script>
import MathJax from "../components/MathJax.vue";
export default {
  components: { MathJax },
  name: "Formalism",
};
</script>

<style scoped>
.final-step {
  transform: scale(0.6);
}

.final-step:hover {
  transform: scale(0.8);
}
</style>
