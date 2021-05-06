#https://pythonexamples.org/
import cv2
import numpy

def filtroBN(foto):
    while True:
        fotoFiltro = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY);
        cv2.imshow('Filtro de blanco y negro', fotoFiltro);

        c = cv2.waitKey(1)
        if c == 13:
            cv2.destroyAllWindows()
            return fotoFiltro;

        if c == 27:
            cv2.destroyAllWindows()
            return foto;

def filtroDifuminar(foto):
    while True:
        fotoFiltro = cv2.blur(foto, (10, 10));
        cv2.imshow('Filtro de blanco y negro', fotoFiltro);

        c = cv2.waitKey(1)
        if c == 13:
            cv2.destroyAllWindows()
            return fotoFiltro;

        if c == 27:
            cv2.destroyAllWindows()
            return foto;

def filtroEspejo(foto):
    while True:
        fotoFiltro = foto;

        fotoFiltro = cv2.flip(foto, 1);

        cv2.imshow('Filtro de espejo', fotoFiltro);

        c = cv2.waitKey(1)

        if c == 13:
            cv2.destroyAllWindows()
            return fotoFiltro;

        if c == 27:
            cv2.destroyAllWindows()
            return foto;

def filtroContraste(foto):
    while True:
        fotoFiltro = cv2.addWeighted(foto, 5, numpy.zeros(foto.shape, foto.dtype), 0, 0)
        cv2.imshow('Brillo', fotoFiltro);

        c = cv2.waitKey(1)
        if c == 13:
            cv2.destroyAllWindows()
            return fotoFiltro;

        if c == 27:
            cv2.destroyAllWindows()
            return foto;
