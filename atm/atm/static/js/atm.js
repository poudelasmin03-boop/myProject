 let pin = '';
        let attempts = 0;
        const correctPin = '1234';
        let balance = 1250;
        let language = 'en';

        function showScreen(screenId) {
            document.querySelectorAll('.screen-content').forEach(el => el.classList.add('hidden'));
            document.getElementById(screenId).classList.remove('hidden');
        }

        function setLanguage(lang) {
            language = lang;
            document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            // In a real app, reload strings based on lang
        }

        function insertCard() {
            showScreen('pin');
        }

        function addPin(digit) {
            if (pin.length < 4) {
                pin += digit;
                document.getElementById('pin-display').textContent = '*'.repeat(pin.length);
            }
        }

        function clearPin() {
            pin = '';
            document.getElementById('pin-display').textContent = '';
        }

        function submitPin() {
            showScreen('loading');
            setTimeout(() => {
                if (pin === correctPin) {
                    showScreen('menu');
                    pin = '';
                    attempts = 0;
                } else {
                    attempts++;
                    if (attempts >= 3) {
                        alert('Card retained. Contact bank.');
                        reset();
                    } else {
                        showScreen('pin');
                        document.querySelector('#pin h2').innerHTML = '<span class="error">Incorrect PIN. Try again.</span>';
                    }
                }
            }, 1000);
        }

        function cancel() { reset(); }
        function selectTransaction(type) { showScreen(type); }
        function backToMenu() { showScreen('menu'); }

        function withdraw(amount) {
            if (balance >= amount) {
                balance -= amount;
                document.getElementById('receipt-text').innerHTML = `Withdrew $${amount}<br>New Balance: $${balance}`;
                showScreen('receipt');
            } else {
                alert('Insufficient funds.');
            }
        }

        function completeDeposit(amount) {
            balance += amount;
            document.getElementById('receipt-text').innerHTML = `Deposited $${amount}<br>New Balance: $${balance}`;
            showScreen('receipt');
        }

        function completeTransfer(amount) {
            if (balance >= amount) {
                balance -= amount;
                document.getElementById('receipt-text').innerHTML = `Transferred $${amount}<br>New Balance: $${balance}`;
                showScreen('receipt');
            } else {
                alert('Insufficient funds.');
            }
        }

        function printReceipt() { alert('Receipt printed.'); }
        function exit() { reset(); }

        function reset() {
            showScreen('welcome');
            pin = '';
            attempts = 0;
            document.getElementById('pin-display').textContent = '';
            document.querySelector('#pin h2').innerHTML = 'Enter PIN';
        }