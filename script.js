document.addEventListener('DOMContentLoaded', () => {
    const imageUpload = document.getElementById('imageUpload');
    const originalImage = document.getElementById('originalImage');
    const transformedImage = document.getElementById('transformedImage');
    const transformationType = document.getElementById('transformationType');
    const transformParam1 = document.getElementById('transformParam1');
    const transformParam2 = document.getElementById('transformParam2');

    // Fungsi untuk membaca gambar
    imageUpload.addEventListener('change', (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();

        reader.onload = (event) => {
            originalImage.src = event.target.result;
        };

        reader.readAsDataURL(file);
    });

    // Fungsi transformasi (placeholder - implementasi aktual membutuhkan backend)
    function transformImage() {
        // Di sini Anda akan memanggil backend/API untuk melakukan transformasi
        console.log('Transformasi:', {
            type: transformationType.value,
            param1: transformParam1.value,
            param2: transformParam2.value
        });
    }

    // Event listener untuk perubahan parameter
    transformationType.addEventListener('change', transformImage);
    transformParam1.addEventListener('input', transformImage);
    transformParam2.addEventListener('input', transformImage);
});