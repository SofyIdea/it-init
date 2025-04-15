document.addEventListener('DOMContentLoaded', function () {
    const statusField = document.querySelector('#id_status'); 
    const cancellationReasonField = document.querySelector('#id_cancellation_reason'); 
    const cancellationReasonRow = cancellationReasonField.closest('.form-row');

    function toggleCancellationReason() {
        if (statusField.value === 'cancelled') {
            cancellationReasonRow.style.display = '';
            cancellationReasonRow.classList.remove('hidden');
        } else {
            cancellationReasonRow.style.display = 'none'; 
            cancellationReasonRow.classList.add('hidden');
            cancellationReasonField.value = ''; 
        }
    }

    toggleCancellationReason();

    statusField.addEventListener('change', toggleCancellationReason);
});