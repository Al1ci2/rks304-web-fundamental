// Ambil elemen form dan semua input
const form = document.getElementById("registerForm");
const username = document.getElementById("username");
const password = document.getElementById("password");
const nama = document.getElementById("nama");
const tanggalLahir = document.getElementById("tanggalLahir");
const alamat = document.getElementById("alamat");
const telepon = document.getElementById("telepon");

function setError(input, message) {
  const errorEl = document.getElementById(input.id + "Error");
  if (message) {
    errorEl.textContent = message;
    errorEl.classList.remove("hidden");
    input.classList.add("border-red-500");
  } else {
    errorEl.textContent = "";
    errorEl.classList.add("hidden");
    input.classList.remove("border-red-500");
  }
  return !message;
}

function validateUsername() {
  const value = username.value.trim();
  if (value === "") return setError(username, "Username tidak boleh kosong");
  if (value.length < 3) return setError(username, "Username minimal 3 karakter");
  return setError(username, "");
}

function validatePassword() {
  const value = password.value;
  if (value === "") return setError(password, "Password tidak boleh kosong");
  if (value.length < 8) return setError(password, "Password minimal 8 karakter");
  return setError(password, "");
}

function validateNama() {
  if (nama.value.trim() === "") return setError(nama, "Nama tidak boleh kosong");
  return setError(nama, "");
}

function validateTanggalLahir() {
  if (tanggalLahir.value === "") {
    return setError(tanggalLahir, "Tanggal lahir tidak boleh kosong");
  }

  const dipilih = new Date(tanggalLahir.value);
  const hariIni = new Date();
  dipilih.setHours(0, 0, 0, 0);
  hariIni.setHours(0, 0, 0, 0);

  if (dipilih > hariIni) {
    return setError(tanggalLahir, "Tanggal lahir tidak boleh di masa depan");
  }
  return setError(tanggalLahir, "");
}

function validateAlamat() {
  if (alamat.value.trim() === "") return setError(alamat, "Alamat tidak boleh kosong");
  return setError(alamat, "");
}

function validateTelepon() {
  const value = telepon.value.trim();
  if (value === "") return setError(telepon, "Nomor telepon tidak boleh kosong");
  if (!value.startsWith("62")) return setError(telepon, "Nomor telepon harus diawali 62");
  return setError(telepon, "");
}

username.addEventListener("input", validateUsername);
password.addEventListener("input", validatePassword);
nama.addEventListener("input", validateNama);
tanggalLahir.addEventListener("change", validateTanggalLahir);
alamat.addEventListener("input", validateAlamat);
telepon.addEventListener("input", validateTelepon);

form.addEventListener("submit", function (event) {
  const semuaValid = [
    validateUsername(),
    validatePassword(),
    validateNama(),
    validateTanggalLahir(),
    validateAlamat(),
    validateTelepon(),
  ].every(Boolean);

  if (!semuaValid) {
    event.preventDefault();
  }
});