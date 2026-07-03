/* ============================================
   Online Voting System - Main JavaScript
   ============================================ */

$(document).ready(function() {

    // ─── Auto-dismiss alerts after 5 seconds ──
    setTimeout(function() {
        $('.alert-dismissible').fadeOut('slow', function() {
            $(this).remove();
        });
    }, 5000);

    // ─── Initialize DataTables ─────────────────
    if ($('#candidatesTable').length) {
        $('#candidatesTable').DataTable({
            order: [[0, 'asc']],
            pageLength: 10,
            language: {
                search: '<i class="fas fa-search"></i>',
            },
            dom: '<"row"<"col-sm-6"l><"col-sm-6"f>>rtip',
        });
    }

    // ─── Sidebar toggle for mobile ─────────────
    $('#sidebarToggle').on('click', function() {
        $('.sidebar').toggleClass('show');
    });

    // Close sidebar on outside click (mobile)
    $(document).on('click', function(e) {
        if ($(window).width() < 992) {
            if (!$(e.target).closest('.sidebar, #sidebarToggle').length) {
                $('.sidebar').removeClass('show');
            }
        }
    });

    // ─── Image upload preview validation ──────
    $('input[type="file"]').on('change', function() {
        const file = this.files[0];
        if (file) {
            // Validate file type
            const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
            if (!allowedTypes.includes(file.type)) {
                showToast('Please select a valid image file (JPEG, PNG, GIF, WebP).', 'warning');
                this.value = '';
                return;
            }
            // Validate file size (max 5MB)
            if (file.size > 5 * 1024 * 1024) {
                showToast('Image size must be less than 5MB.', 'warning');
                this.value = '';
                return;
            }
        }
    });

    // ─── Smooth scroll to hash links ──────────
    $('a[href^="#"]').on('click', function(e) {
        const target = $(this.getAttribute('href'));
        if (target.length) {
            e.preventDefault();
            $('html, body').animate({ scrollTop: target.offset().top - 80 }, 500);
        }
    });

});

// ─── Global Toast Function ─────────────────
function showToast(message, type) {
    type = type || 'info';
    const icons = {
        success: 'fa-check-circle',
        danger: 'fa-exclamation-circle',
        warning: 'fa-exclamation-triangle',
        info: 'fa-info-circle'
    };

    const toastHtml = `
        <div class="toast align-items-center text-bg-${type} border-0 show" role="alert" style="min-width:300px;">
            <div class="d-flex">
                <div class="toast-body">
                    <i class="fas ${icons[type] || icons.info} me-2"></i>${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" onclick="this.closest('.toast').remove()"></button>
            </div>
        </div>
    `;

    let container = document.getElementById('toastContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
        document.body.appendChild(container);
    }

    container.insertAdjacentHTML('beforeend', toastHtml);
    setTimeout(function() {
        const toasts = container.querySelectorAll('.toast');
        if (toasts.length) toasts[toasts.length - 1].remove();
    }, 4000);
}
