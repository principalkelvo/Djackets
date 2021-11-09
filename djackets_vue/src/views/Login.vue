<template>
  <section id="cover" class="min-vh-100">
    <div id="cover-caption">
      <div class="container">
        <div class="columns">
          <div class="column is-4 is-offset-4">
            <h1 class="title">Login</h1>
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
  name: "Login",
};
</script>
