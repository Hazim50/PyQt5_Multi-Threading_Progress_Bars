<h1>[EN]</h1>
<h2>PyQt5 Multi-Threading Progress Bars</h2>

<p>This project contains an example of designing an interface using the PyQt5 library and updating progress bars using multiple threads.</p>

<h3>How It Works</h3>

<ul>
    <li>There are three "Start" buttons on the main window. Each button starts a thread and updates a progress bar.</li>
    <li>Each thread increments a counter at a specific time interval and communicates this value to the main window by sending a signal.</li>
    <li>The main window receives the signal and updates the progress bar based on the sender's identity.</li>
    <li>Each thread has a corresponding "Stop" button to halt the thread.</li>
</ul>

<h3>Requirements</h3>

<ul>
    <li>Python 3.x</li>
    <li>PyQt5</li>
</ul>

<h3>Installation</h3>

<ol>
    <li>Clone the repository or download the ZIP file:</li>
    <code>git clone https://github.com/Hazim50/PyQt5-MultiThreading-ProgressBar.git</code>
    <li>Install the required libraries:</li>
    <code>pip install PyQt5</code>
    <li>Run the code:</li>
    <code>python PyQt5_Multi-Threading_Progress_Bars.py</code>
</ol>

<h1>[TR]</h1>
<h2>PyQt5 Çoklu İş Parçacığı İlerleme Çubukları</h2>

<p>Bu proje, PyQt5 kütüphanesini kullanarak bir arayüz tasarlama örneği içerir ve birden çok iş parçacığı kullanarak ilerleme çubuklarını günceller.</p>

<h3>Nasıl Çalışır</h3>

<ul>
    <li>Ana pencerede üç "Başlat" düğmesi bulunmaktadır. Her düğme bir iş parçacığını başlatır ve bir ilerleme çubuğunu günceller.</li>
    <li>Her iş parçacığı, belirli bir zaman aralığında bir sayacı artırır ve bu değeri bir sinyal göndererek ana pencereye iletir.</li>
    <li>Ana pencere, sinyali alır ve ilerleme çubuğunu gönderenin kimliğine dayanarak günceller.</li>
    <li>Her iş parçacığının durdurulması için bir karşılık gelen "Durdur" düğmesi bulunmaktadır.</li>
</ul>

<h3>Gereksinimler</h3>

<ul>
    <li>Python 3.x</li>
    <li>PyQt5</li>
</ul>

<h3>Kurulum</h3>

<ol>
    <li>Depoyu klonlayın veya ZIP dosyasını indirin:</li>
    <code>git clone https://github.com/Hazim50/PyQt5-MultiThreading-ProgressBar.git</code>
    <li>Gerekli kütüphaneleri yükleyin:</li>
    <code>pip install PyQt5</code>
    <li>Kodu çalıştırın:</li>
    <code>python PyQt5_Multi-Threading_Progress_Bars.py</code>
</ol>
