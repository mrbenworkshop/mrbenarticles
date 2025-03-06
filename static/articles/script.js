document.querySelectorAll(".toTop").forEach(anchor => {
    anchor.addEventListener("click", function (event) {
        event.preventDefault();
        let targetId = this.getAttribute("href").substring(1);
        document.getElementById(targetId).scrollIntoView({ behavior: "smooth" });
    });
});

const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')      // Replace & symbol with '-and-'
        .replace(/[\s\W-]+/g, '-')   // Replace spaces, non-word characters, and dashes with '-'
};

const checkSlugAvailability = async (slug) => {
    try {
        let response = await fetch(`/check-slug?slug=${slug}`);
        let data = await response.json();
        return data.exists;  // Returns true if slug already exists
    } catch (error) {
        console.error("Error checking slug:", error);
        return false; // Assume slug is available if an error occurs
    }
};

titleInput.addEventListener('keyup', async (e) => {
    let baseSlug = slugify(titleInput.value);
    let uniqueSlug = baseSlug;
    let counter = 1;

    while (await checkSlugAvailability(uniqueSlug)) {
        uniqueSlug = `${baseSlug}-${counter}`;
        counter++;
    }

    slugInput.setAttribute('value', uniqueSlug);
});