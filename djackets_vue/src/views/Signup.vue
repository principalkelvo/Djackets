<template>
  <section id="cover" class="min-vh-100">
    <div id="cover-caption">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <h1 class="title">Sign up</h1>
            <form>
              <div class="field">
                <label>Email</label>
                <div class="conrol">
                  <input type="email" name="email" class="input" placeholder="Email" />
                </div>
              </div>
              <div class="field">
                <label>Password</label>
                <div class="conrol">
                  <input type="password" name="password" class="input" placeholder="Password" />
                </div>
              </div>
              <div class="field">
                <label>Confirm password</label>
                <div class="conrol">
                  <input type="password" name="password1" class="input" placeholder="Confirm Password" />
                </div>
              </div>
              <div class="field">
                <div class="conrol">
                  <button class="button is-success">Submit</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "SignUp",
};
</script>

<style>
#cover {
    background: #222 url('https://unsplash.it/1920/1080/?random') center center no-repeat;
    background-size: cover;
    height: 100%;
    text-align: center;
    display: flex;
    align-items: center;
    position: relative;
}

#cover-caption {
    width: 100%;
    position: relative;
    z-index: 1;
}

/* only used for background overlay not needed for centering */
form:before {
    content: '';
    height: 100%;
    left: 18%;
    position: absolute;
    top: 0;
    width: 65%;
    background-color: rgba(0,0,0,0.3);
    z-index: -1;
    border-radius: 10px;
}
</style>
