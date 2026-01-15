let currentPage = 1;
let editingEmployeeId = null;

let selectedDepartment = "";
let selectedRole = "";

const tableBody = document.getElementById("employee-table");
const pageInfo = document.getElementById("page-info");
const form = document.getElementById("employee-form");
const modalTitle = document.getElementById("modal-title");

const departmentFilter = document.getElementById("filter-department");
const roleFilter = document.getElementById("filter-role");

const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");

const modal = new bootstrap.Modal(
    document.getElementById("employeeModal")
);

const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const departmentInput = document.getElementById("department");
const roleInput = document.getElementById("role");

function buildQueryParams() {
    const params = new URLSearchParams();
    params.append("page", currentPage);

    if (selectedDepartment) {
        params.append("department", selectedDepartment);
    }
    if (selectedRole) {
        params.append("role", selectedRole);
    }

    return params.toString();
}

function loadEmployees() {
    fetch(`/api/employees/?${buildQueryParams()}`)
        .then(res => res.json())
        .then(data => {
            tableBody.innerHTML = "";

            data.results.forEach(emp => {
                tableBody.innerHTML += `
                    <tr>
                        <td>${emp.id}</td>
                        <td>${emp.name}</td>
                        <td>${emp.email}</td>
                        <td>${emp.department || ""}</td>
                        <td>${emp.role || ""}</td>
                        <td>
                            <button class="btn btn-warning btn-sm me-2"
                                onclick='openEditModal(${JSON.stringify(emp)})'>
                                Edit
                            </button>
                            <button class="btn btn-danger btn-sm"
                                onclick="deleteEmployee(${emp.id})">
                                Delete
                            </button>
                        </td>
                    </tr>
                `;
            });

            pageInfo.innerText =
                `Page ${data.current_page} of ${data.total_pages}`;

            prevBtn.disabled = currentPage === 1;
            nextBtn.disabled = currentPage === data.total_pages;
        });
}

function applyFilters() {
    selectedDepartment = departmentFilter.value;
    selectedRole = roleFilter.value;
    currentPage = 1;
    loadEmployees();
}

function clearFilters() {
    departmentFilter.value = "";
    roleFilter.value = "";
    selectedDepartment = "";
    selectedRole = "";
    currentPage = 1;
    loadEmployees();
}

function openAddModal() {
    editingEmployeeId = null;
    modalTitle.innerText = "Add Employee";
    form.reset();
}

function openEditModal(employee) {
    editingEmployeeId = employee.id;
    modalTitle.innerText = "Edit Employee";

    nameInput.value = employee.name;
    emailInput.value = employee.email;
    departmentInput.value = employee.department || "";
    roleInput.value = employee.role || "";

    modal.show();
}

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const payload = {
        name: nameInput.value,
        email: emailInput.value,
        department: departmentInput.value,
        role: roleInput.value
    };

    const url = editingEmployeeId
        ? `/api/employees/${editingEmployeeId}/`
        : `/api/employees/`;

    const method = editingEmployeeId ? "PUT" : "POST";

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    }).then(response => {
        if (!response.ok) {
            alert("Error saving employee");
            return;
        }
        form.reset();
        modal.hide();
        loadEmployees();
    });
});

function deleteEmployee(id) {
    fetch(`/api/employees/${id}/`, { method: "DELETE" })
        .then(() => loadEmployees());
}

prevBtn.addEventListener("click", () => {
    if (currentPage > 1) {
        currentPage--;
        loadEmployees();
    }
});

nextBtn.addEventListener("click", () => {
    currentPage++;
    loadEmployees();
});

loadEmployees();
