<template>
  <div class="blog">
    <h1>{{ $route.name }}</h1>
    <p>
      If you want to send some piece of information to
      <it>only</it> your friend and no one else, then you will have to have some
      technique to ensure that no one else is able to read this piece of
      information. This is where the concept of <it>encryption</it> comes in.
      Encryption is the process of converting a message into a secret coded form
      that cannot be read without knowing how to decode the secret coded form
      back into the original message. There are two important takeaways from
      this section about encryption. First of all, understanding how asymmetric
      key encryption works in general. And secondly, why we cannot decode parts
      of a message that have been encrypted using the asymmetric encryption
      algorithm.
    </p>

    <p>
      At their core, the encryption algorithms can be defined as the symmetric
      technique having only one key, while the asymmetric technique has two
      keys. Symmetric encryption uses one key in order to
      <it CLASS="textit">both</it> lock and unlock a piece of information.
      Asymmetric encryption uses one key in order to lock the information and
      another key to unlock the information. Symmetric keys are generally not
      preferred as they can be easily copied or stolen, especially when they are
      being transferred to someone else who would need to decrypt the
      information that you send them. Not only would this mean that the message
      could be decrypted by someone else. It also means that there is no way in
      which the receiver of a message can be sure that the message comes from
      the original sender. This leaves us with asymmetric encryption.
    </p>

    <p>Asymmetric encryption generally works as follows:</p>

    <ul>
      <li>
        There is a key that locks information which can be send out into public.
        Everyone can have access to the public key.
      </li>
      <li>
        There is another key which is kept private and will be used for
        unlocking any information that was locked using the public key.
      </li>
    </ul>

    <p>
      This asymmetric key-pair gives a secure way for agents to send information
      back and forth (as long as both agents have a secure asymmetric key-pair
      of each other). Take for instance, Alice (on the left) and Bob (on the
      right) below. Bob wants to send a message, Alice can encrypt it with her
      public key and decrypt it with her private key.
    </p>

    <div class="image encryptiongif"></div>

    <p>
      Understanding the basic process of asymmetric cryptography is important in
      order to understand the epistemic logic that follows from it, specifically
      for the interlock protocol. However, to understand the Interlock protocol
      that will be explained later, we need to have an understanding about why
      we cannot decode half of an encoded message.
    </p>
    <p>
      The other realisation that is important is that we need the entire
      encrypted message in order to decode it. If we break it into two, and
      decode one of the halves, we get gibberish back. Somewhat of an analogy
      might be found in breaking a lock in two. It becomes hard to unlock a half
      of a lock simply because it is broken. With digital locks, a broken lock
      cannot be unlocked (unlike real life where a broken lock does unlock the
      thing hiding behind it).
    </p>

    <p>
      The following section has been added for completeness' sake. It describes
      an example of how RSA (an asymmetric encryption algorithm) works. We left
      this in as it might help better understand encryption. The next section
      (hiding under the button) can safely be skipped, if encryption is clear.
    </p>

    <p>
      <button
        type="button"
        v-on:click="toggleCollapsible"
        :class="{ collapsible: true, active: isShowingCollapsible }"
      >
        Show Example Encryption Algorithm
      </button>
    </p>
    <div
      :class="{
        content: !isShowingCollapsible,
        'content-not-hidden': isShowingCollapsible,
      }"
    >
      <h2>An Example Encryption Algorithm</h2>

      <p>
        Underlying asymmetric public key cryptography is an encryption algorithm
        which relies on a lot of complex mathematical properties. RSA&nbsp; is
        such an encryption algorithm that can be used for asymmetric
        cryptography. The step-by-step process on how this algorithm works is
        given below.
      </p>

      <p>
        First we will have to generate a RSA key-pair. We can do that as
        follows:
      </p>

      <ol>
        <li>
          Choose 2 large prime number <it>p</it> and <it>q</it>. As an example
          we can take:
          <math-jax :formula="'$$p=61$$'"></math-jax>
          <math-jax :formula="'$$q=79$$'"></math-jax>
        </li>
        <li>
          Compute
          <math-jax :formula="'$n = p q$'"></math-jax>
          and
          <math-jax :formula="'$z = (p-1) (q - 1)$'"></math-jax>
          <math-jax :formula="'$$n = 61 * 79 = 4819$$'"></math-jax>
          <math-jax :formula="'$$z = (61-1)(79-1)=60 * 78 = 4680$$'"></math-jax>
        </li>
        <li>
          Choose <it>e</it> such that
          <math-jax :formula="'$e < z$'"> </math-jax> and that <it>e</it> has no
          common factors with <it>z</it>.
          <br />
          <math-jax :formula="'$$e = 19$$'"></math-jax>
        </li>
        <li>
          Choose <it>d</it> such that <math-jax :formula="'ed - 1'" /> is
          exactly divisible by <it>z</it>.
          <math-jax :formula="'$$d = 739$$'"></math-jax>
        </li>
        <li>
          Now we have our public key as
          <math-jax :formula="'$(n, e)$'"></math-jax>
          and our private key as
          <math-jax :formula="'$(n, d)$'"></math-jax>
          <math-jax :formula="'$$Key_{public} = (4819,19)$$'"></math-jax>
          <math-jax :formula="'$$Key_{private} = (4819,739)$$'"></math-jax>
        </li>
      </ol>

      <p>
        Now that we have a public and private key-pair, we can encrypt and
        decrypt messages. In order to encrypt a message, the message first needs
        to be transformed into a numerical value. If we were now to encrypt the
        message "Cuddly Llamas", then we would get the following example:
      </p>

      <ol>
        <li>
          First, we transform "Cuddly Llamas" into its binary value
          representation (using ASCII):
          <pre>
        0100001101110101011001000110010001101100011110010010000
        0010011000110110001100001011011010110000101110011
</pre
          >
        </li>
        <li>
          Then encrypt the numerical representation using
          <math-jax :formula="'$C = m ^ e (mod N)$'"></math-jax> for the
          message, resulting in:
          <pre>
        0001100101011100010011011100101111001010010111100101000
        1011001110011010001101000000010110101000100100011000101
        1001110011010110101110001000110110110101101011100011010
        0100
</pre
          >
          Note that the if we take half of the encrypted message, it will
          decrypt to something else than "Cuddly".
          <br />
          <br />
        </li>
        <li>
          Decrypting the encrypted message using
          <math-jax :formula="'$m = C ^ d (mod N)$'"></math-jax>
          would result in the original message:
          <pre>
        0100001101110101011001000110010001101100011110010010000
        0010011000110110001100001011011010110000101110011
</pre
          >
        </li>
        <li>
          Transforming this numerical result back into text gives:
          <pre>
        Cuddly Llamas
</pre
          >
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
import MathJax from "../components/MathJax.vue";
export default {
  components: { MathJax },
  name: "Encryption",
  data() {
    return {
      isShowingCollapsible: false,
    };
  },
  mounted() {
    try {
      window.MathJax.typeset();
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    toggleCollapsible: function toggleCollapsible() {
      console.log("collapsing toggle");
      this.isShowingCollapsible = !this.isShowingCollapsible;
    },
  },
};
</script>

<style scoped>
.encryptiongif {
  background: url("../assets/img/asym-encryption-static.png");
  width: 896px;
  height: 179px;
}

.encryptiongif:hover {
  background: url("../assets/img/asym-encryption.gif");
  cursor: pointer;
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

@media (max-width: 767px) {
  .encryptiongif {
    width: 194px;
    height: 157px;
    background: url("../assets/img/gif-not-supported-message.jpg");
  }

  .encryptiongif:hover {
    background: url("../assets/img/gif-not-supported-message.jpg");
    cursor: pointer;
  }
}
</style>
