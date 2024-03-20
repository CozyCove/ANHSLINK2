document.addEventListener("DOMContentLoaded", load);
function load() {
  fetch("/room")
    .then((response) => response.json())
    .then((data) => {
      console.log(data.rooms);
      data.rooms.length != 0 ? console.log("naa") : console.log("wala");
      data.rooms.forEach(show);
    });
}
function show(rooms) {
  const roomDiv = document.getElementById("rooms");
  const room = document.createElement("div");
  console.log(rooms);
  room.innerHTML =
    rooms && Object.keys(rooms).length > 0
      ? `
     
      <article
      class="rounded-lg border border-gray-100 bg-white p-4 shadow-sm transition hover:shadow-lg sm:p-6 max-w-50"
    >
      <span class="inline-block rounded text-black"
        >Teacher: ${rooms.teacher.user.username}
      </span>
    
      <a href="#">
        <h3 class="mt-0.5 text-lg font-medium text-gray-900">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit.
        </h3>
      </a>
    
      <p class="mt-2 line-clamp-3 text-sm/relaxed text-gray-500">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae
        dolores, possimus pariatur animi temporibus nesciunt praesentium dolore sed
        nulla ipsum eveniet corporis quidem, mollitia itaque minus soluta,
        voluptates neque explicabo tempora nisi culpa eius atque dignissimos.
        Molestias explicabo corporis voluptatem?
      </p>
    
      <div class="flex justify-between mt-4">
        <a
          href="#"
          class="group inline-flex items-center gap-1 text-sm font-medium text-blue-600"
        >
          Go to classroom
          <span
            aria-hidden="true"
            class="block transition-all group-hover:ms-0.5 rtl:rotate-180"
          >
            &rarr;
          </span>
        </a>
        <div></div>
      <div class="flex align-middle">
      <div class="flex items-center"><svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      height="20"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="feather feather-user"
    >
      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
      <circle cx="12" cy="7" r="4"></circle>
    </svg></div>
     <div>${rooms.student_count}</div>
      

      </div>
        
      </div>
    </article>


      <div class="bg-black"></div>
      Name: ${rooms.name} Students: `
      : `waysud`;
  roomDiv.appendChild(room);
}
